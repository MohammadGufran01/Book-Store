import logging
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from django.contrib.auth.models import User
from books.models import Book, Review, BookInteraction
from orders.models import OrderItem
from cart.models import Wishlist

logger = logging.getLogger(__name__)


def build_interaction_matrix():
    """
    Constructs a DataFrame representing user-item interaction scores.
    Combines explicit ratings (1-5), purchases (4.5), wishlists (3.5), and views (1.5).
    """
    records = []

    # 1. Explicit reviews
    for rev in Review.objects.select_related('user', 'book'):
        records.append({
            'user_id': rev.user_id,
            'book_id': rev.book_id,
            'score': float(rev.rating)
        })

    # 2. Purchases
    for item in OrderItem.objects.filter(order__user__isnull=False).select_related('order', 'book'):
        if item.book_id and item.order.user_id:
            records.append({
                'user_id': item.order.user_id,
                'book_id': item.book_id,
                'score': 4.5
            })

    # 3. Wishlists
    for w in Wishlist.objects.all():
        records.append({
            'user_id': w.user_id,
            'book_id': w.book_id,
            'score': 3.5
        })

    # 4. Implicit interactions
    for bi in BookInteraction.objects.filter(user__isnull=False):
        weight = 1.5 if bi.interaction_type == 'view' else (3.0 if bi.interaction_type == 'cart' else bi.score)
        records.append({
            'user_id': bi.user_id,
            'book_id': bi.book_id,
            'score': weight
        })

    if not records:
        return pd.DataFrame(), [], []

    df = pd.DataFrame(records)
    # Take max score if multiple interactions exist for same (user, book)
    df = df.groupby(['user_id', 'book_id'])['score'].max().reset_index()

    user_ids = sorted(df['user_id'].unique().tolist())
    book_ids = sorted(df['book_id'].unique().tolist())

    pivot_matrix = df.pivot(index='user_id', columns='book_id', values='score').fillna(0.0)
    return pivot_matrix, user_ids, book_ids


def get_user_collaborative_recommendations(user, limit=8, exclude_ids=None):
    """
    Predicts book ratings for a user using User-to-User Collaborative Filtering.
    Finds nearest neighbor users with similar taste and recommends items they loved.
    """
    if exclude_ids is None:
        exclude_ids = set()

    try:
        matrix, user_ids, book_ids = build_interaction_matrix()
        if matrix.empty or user.id not in matrix.index or len(user_ids) < 2:
            return []

        user_vector = matrix.loc[[user.id]].values
        all_users = matrix.values

        # Compute cosine similarity between target user and all other users
        user_similarities = cosine_similarity(user_vector, all_users).flatten()
        user_idx = user_ids.index(user.id)
        user_similarities[user_idx] = 0.0 # Exclude self

        # Find top similar users with positive similarity
        top_neighbor_indices = np.argsort(user_similarities)[::-1]
        top_neighbor_indices = [idx for idx in top_neighbor_indices if user_similarities[idx] > 0.05][:10]

        if not top_neighbor_indices:
            return []

        # Find books the target user has already interacted with
        user_interacted_book_ids = set(matrix.columns[matrix.loc[user.id] > 0])
        exclude_ids.update(user_interacted_book_ids)

        predicted_scores = {}
        for book_id in matrix.columns:
            if book_id in exclude_ids:
                continue

            sim_sum = 0.0
            weighted_rating_sum = 0.0

            for n_idx in top_neighbor_indices:
                neighbor_user_id = user_ids[n_idx]
                neighbor_sim = user_similarities[n_idx]
                neighbor_rating = matrix.loc[neighbor_user_id, book_id]

                if neighbor_rating > 0:
                    weighted_rating_sum += neighbor_sim * neighbor_rating
                    sim_sum += neighbor_sim

            if sim_sum > 0:
                predicted_scores[book_id] = weighted_rating_sum / sim_sum

        if not predicted_scores:
            return []

        sorted_books = sorted(predicted_scores.items(), key=lambda x: x[1], reverse=True)[:limit]
        candidate_ids = [b_id for b_id, _ in sorted_books]
        
        book_objects = {b.id: b for b in Book.objects.filter(id__in=candidate_ids, is_active=True).prefetch_related('genres', 'author')}

        results = []
        for b_id, pred_score in sorted_books:
            if b_id in book_objects:
                results.append({
                    'book': book_objects[b_id],
                    'score': round(min(pred_score / 5.0, 1.0) * 100, 1),
                    'reason': "Readers with similar taste enjoyed this",
                    'algorithm': 'Collaborative Filtering (User-User)'
                })

        return results
    except Exception as e:
        logger.error(f"Collaborative filtering recommendation error: {e}")
        return []


def get_item_collaborative_similar_books(target_book, limit=6, exclude_ids=None):
    """
    Item-to-Item Collaborative Filtering:
    Finds books that have similar user interaction patterns to the target book.
    """
    if exclude_ids is None:
        exclude_ids = set()
    exclude_ids.add(target_book.id)

    try:
        matrix, user_ids, book_ids = build_interaction_matrix()
        if matrix.empty or target_book.id not in matrix.columns or len(book_ids) < 2:
            return []

        item_matrix = matrix.T # Shape: (n_books, n_users)
        target_idx = list(item_matrix.index).index(target_book.id)
        
        target_vector = item_matrix.iloc[[target_idx]].values
        all_items = item_matrix.values

        sim_scores = cosine_similarity(target_vector, all_items).flatten()
        sim_scores[target_idx] = 0.0

        ranked_indices = np.argsort(sim_scores)[::-1]
        results = []

        candidate_ids = []
        scores_map = {}
        for idx in ranked_indices:
            b_id = item_matrix.index[idx]
            if b_id in exclude_ids:
                continue
            score = float(sim_scores[idx])
            if score > 0.05:
                candidate_ids.append(b_id)
                scores_map[b_id] = score
            if len(candidate_ids) >= limit:
                break

        if not candidate_ids:
            return []

        book_objects = {b.id: b for b in Book.objects.filter(id__in=candidate_ids, is_active=True).prefetch_related('genres', 'author')}

        for b_id in candidate_ids:
            if b_id in book_objects:
                results.append({
                    'book': book_objects[b_id],
                    'score': round(scores_map[b_id] * 100, 1),
                    'reason': f"Readers who liked '{target_book.title}' also enjoyed",
                    'algorithm': 'Collaborative Filtering (Item-Item)'
                })

        return results
    except Exception as e:
        logger.error(f"Item collaborative similarity error: {e}")
        return []
