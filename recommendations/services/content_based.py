import logging
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from books.models import Book, Review

logger = logging.getLogger(__name__)


def build_book_corpus(books):
    """
    Constructs rich text representations for books incorporating
    title, author name, genres, synopsis, format, and publisher.
    """
    corpus = []
    for b in books:
        genres_str = " ".join([g.name for g in b.genres.all()])
        # Weighting title, author, and genres by repeating them in the document representation
        text = f"{b.title} {b.title} {b.author.name} {b.author.name} {genres_str} {genres_str} {b.format} {b.publisher} {b.synopsis}"
        corpus.append(text)
    return corpus


def get_content_based_similar_books(target_book, limit=6, exclude_ids=None):
    """
    Given a target book, calculates TF-IDF cosine similarity against all active books in the catalog.
    Returns list of dicts: [{'book': book_obj, 'score': similarity_score, 'reason': 'Similar Genre & Author'}]
    """
    if exclude_ids is None:
        exclude_ids = set()
    exclude_ids.add(target_book.id)

    books = list(Book.objects.filter(is_active=True).prefetch_related('genres', 'author'))
    if not books or len(books) < 2:
        return []

    # Map book id to index
    id_to_idx = {b.id: i for i, b in enumerate(books)}
    if target_book.id not in id_to_idx:
        return []

    target_idx = id_to_idx[target_book.id]
    corpus = build_book_corpus(books)

    try:
        tfidf = TfidfVectorizer(stop_words='english', max_features=5000, ngram_range=(1, 2))
        tfidf_matrix = tfidf.fit_transform(corpus)
        
        # Cosine similarity for target book
        target_vector = tfidf_matrix[target_idx]
        sim_scores = cosine_similarity(target_vector, tfidf_matrix).flatten()

        # Sort descending by score
        ranked_indices = np.argsort(sim_scores)[::-1]
        
        results = []
        for idx in ranked_indices:
            candidate = books[idx]
            if candidate.id in exclude_ids:
                continue
            
            score = float(sim_scores[idx])
            # Determine reason
            shared_genres = set(target_book.genres.values_list('name', flat=True)).intersection(
                set(candidate.genres.values_list('name', flat=True))
            )
            same_author = target_book.author_id == candidate.author_id
            
            if same_author:
                reason = f"More by {target_book.author.name}"
            elif shared_genres:
                reason = f"Shares {', '.join(list(shared_genres)[:2])}"
            else:
                reason = "Similar plot & themes"

            results.append({
                'book': candidate,
                'score': round(score * 100, 1),
                'reason': reason,
                'algorithm': 'Content-Based (TF-IDF)'
            })

            if len(results) >= limit:
                break

        return results
    except Exception as e:
        logger.error(f"Content-based similarity error: {e}")
        # Fallback to same genre / author books
        fallback_books = Book.objects.filter(
            is_active=True,
            genres__in=target_book.genres.all()
        ).exclude(id__in=exclude_ids).distinct()[:limit]
        
        return [{
            'book': b,
            'score': 85.0,
            'reason': f"Matches genre {target_book.genres.first().name if target_book.genres.exists() else ''}",
            'algorithm': 'Genre-Match'
        } for b in fallback_books]


def get_content_based_user_recommendations(user, limit=8, exclude_ids=None):
    """
    Computes a personalized user profile vector by aggregating text of books
    the user has highly rated (>=4 stars), purchased, or wishlisted.
    """
    if exclude_ids is None:
        exclude_ids = set()

    # Find books the user interacted with positively
    from cart.models import Wishlist
    from orders.models import OrderItem
    
    rated_positive_book_ids = list(Review.objects.filter(user=user, rating__gte=4).values_list('book_id', flat=True))
    purchased_book_ids = list(OrderItem.objects.filter(order__user=user).values_list('book_id', flat=True))
    wishlisted_book_ids = list(Wishlist.objects.filter(user=user).values_list('book_id', flat=True))

    user_liked_ids = list(set(rated_positive_book_ids + purchased_book_ids + wishlisted_book_ids))
    exclude_ids.update(user_liked_ids)

    if not user_liked_ids:
        return []

    all_books = list(Book.objects.filter(is_active=True).prefetch_related('genres', 'author'))
    if not all_books:
        return []

    id_to_idx = {b.id: i for i, b in enumerate(all_books)}
    corpus = build_book_corpus(all_books)

    try:
        tfidf = TfidfVectorizer(stop_words='english', max_features=5000, ngram_range=(1, 2))
        tfidf_matrix = tfidf.fit_transform(corpus)

        # Build user vector as weighted average
        user_vector = np.zeros((1, tfidf_matrix.shape[1]))
        total_weight = 0

        for book_id in user_liked_ids:
            if book_id in id_to_idx:
                idx = id_to_idx[book_id]
                weight = 1.0
                if book_id in rated_positive_book_ids:
                    weight = 2.0
                elif book_id in purchased_book_ids:
                    weight = 1.5
                
                user_vector += weight * tfidf_matrix[idx].toarray()
                total_weight += weight

        if total_weight > 0:
            user_vector /= total_weight

        sim_scores = cosine_similarity(user_vector, tfidf_matrix).flatten()
        ranked_indices = np.argsort(sim_scores)[::-1]

        results = []
        for idx in ranked_indices:
            candidate = all_books[idx]
            if candidate.id in exclude_ids:
                continue

            score = float(sim_scores[idx])
            if score <= 0.01:
                continue

            # Pick a liked book to explain "Because you liked X"
            explanation = "Tailored to your reading tastes"
            if rated_positive_book_ids:
                reference_book = Book.objects.filter(id=rated_positive_book_ids[0]).first()
                if reference_book:
                    explanation = f"Because you loved '{reference_book.title}'"
            elif purchased_book_ids:
                reference_book = Book.objects.filter(id=purchased_book_ids[0]).first()
                if reference_book:
                    explanation = f"Because you purchased '{reference_book.title}'"

            results.append({
                'book': candidate,
                'score': round(score * 100, 1),
                'reason': explanation,
                'algorithm': 'Content-Based Profile'
            })

            if len(results) >= limit:
                break

        return results
    except Exception as e:
        logger.error(f"User content-based recommendation error: {e}")
        return []
