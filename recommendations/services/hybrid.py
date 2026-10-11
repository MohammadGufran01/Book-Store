import logging
from django.db.models import Avg, Count
from books.models import Book, Review, Genre
from .content_based import get_content_based_user_recommendations
from .collaborative import get_user_collaborative_recommendations

logger = logging.getLogger(__name__)


def calculate_bayesian_rating(book, min_votes=2, global_mean=4.0):
    """
    Computes IMDB-style Bayesian weighted rating to prevent books with 1 review of 5★
    from unduly outranking books with 50 reviews of 4.8★.
    """
    v = book.review_count
    if v == 0:
        return 0.0
    r = book.average_rating
    return (v / (v + min_votes)) * r + (min_votes / (v + min_votes)) * global_mean


def get_popular_trending_books(limit=8, exclude_ids=None):
    """
    Returns trending and top-rated books using Bayesian rating and sales popularity.
    """
    if exclude_ids is None:
        exclude_ids = set()

    books = Book.objects.filter(is_active=True).exclude(id__in=exclude_ids).prefetch_related('genres', 'author')
    if not books.exists():
        return []

    # Calculate global mean rating
    avg_data = Review.objects.aggregate(Avg('rating'))
    global_mean = float(avg_data['rating__avg'] or 4.0)

    scored_books = []
    for b in books:
        bayesian_score = calculate_bayesian_rating(b, min_votes=2, global_mean=global_mean)
        # Bonus if bestseller or featured
        bonus = 0.5 if b.is_bestseller else (0.25 if b.is_featured else 0.0)
        final_score = bayesian_score + bonus
        
        scored_books.append((b, final_score))

    scored_books.sort(key=lambda x: x[1], reverse=True)
    top_books = scored_books[:limit]

    results = []
    for b, score in top_books:
        results.append({
            'book': b,
            'score': round(min(score / 5.5, 1.0) * 100, 1),
            'reason': "Top rated bestseller across the bookstore",
            'algorithm': 'Bayesian Popularity'
        })
    return results


def get_cold_start_recommendations(user, limit=8, exclude_ids=None):
    """
    Provides curated onboarding recommendations for users without purchase/rating history.
    Uses profile's favorite genres if available, or top books across all genres.
    """
    if exclude_ids is None:
        exclude_ids = set()

    results = []
    if user and user.is_authenticated and hasattr(user, 'profile'):
        fav_genres = list(user.profile.favorite_genres.all())
        if fav_genres:
            books_in_favs = Book.objects.filter(
                is_active=True,
                genres__in=fav_genres
            ).exclude(id__in=exclude_ids).distinct().prefetch_related('genres', 'author')[:limit]

            for b in books_in_favs:
                matched_genres = [g.name for g in fav_genres if g in b.genres.all()]
                results.append({
                    'book': b,
                    'score': 90.0,
                    'reason': f"Matches your chosen interest in {', '.join(matched_genres)}",
                    'algorithm': 'Onboarding Preference Match'
                })
                exclude_ids.add(b.id)

    if len(results) < limit:
        remaining_needed = limit - len(results)
        popular = get_popular_trending_books(limit=remaining_needed, exclude_ids=exclude_ids)
        results.extend(popular)

    return results[:limit]


def get_hybrid_recommendations_for_user(user, limit=8, exclude_ids=None):
    """
    Hybrid Recommendation Engine:
    Blends Collaborative Filtering (40%), Content-Based Filtering (40%), and Popularity (20%).
    Gracefully falls back to Cold-Start and Popularity when user has few interactions.
    """
    if exclude_ids is None:
        exclude_ids = set()

    if not user or not user.is_authenticated:
        return get_popular_trending_books(limit=limit, exclude_ids=exclude_ids)

    # 1. Fetch collaborative recommendations
    collab_results = get_user_collaborative_recommendations(user, limit=limit * 2, exclude_ids=set(exclude_ids))
    collab_dict = {item['book'].id: item for item in collab_results}

    # 2. Fetch content-based recommendations
    content_results = get_content_based_user_recommendations(user, limit=limit * 2, exclude_ids=set(exclude_ids))
    content_dict = {item['book'].id: item for item in content_results}

    # If user has neither collaborative nor content signals (new user), use cold start
    if not collab_dict and not content_dict:
        return get_cold_start_recommendations(user, limit=limit, exclude_ids=exclude_ids)

    all_candidate_ids = set(collab_dict.keys()).union(set(content_dict.keys()))

    # 3. Calculate blended hybrid scores
    blended_scores = []
    for b_id in all_candidate_ids:
        collab_score = collab_dict.get(b_id, {}).get('score', 40.0) if collab_dict else 50.0
        content_score = content_dict.get(b_id, {}).get('score', 40.0) if content_dict else 50.0

        # Weights: 45% collab, 45% content, 10% base
        final_score = (0.45 * collab_score) + (0.45 * content_score) + 10.0

        # Best explanation
        if b_id in collab_dict and b_id in content_dict:
            reason = f"Highly matched to your reading history & readers like you"
            algorithm = 'Hybrid (Collaborative + Content-Based)'
            book_obj = collab_dict[b_id]['book']
        elif b_id in content_dict:
            reason = content_dict[b_id]['reason']
            algorithm = content_dict[b_id]['algorithm']
            book_obj = content_dict[b_id]['book']
        else:
            reason = collab_dict[b_id]['reason']
            algorithm = collab_dict[b_id]['algorithm']
            book_obj = collab_dict[b_id]['book']

        blended_scores.append({
            'book': book_obj,
            'score': round(min(final_score, 99.0), 1),
            'reason': reason,
            'algorithm': algorithm
        })

    blended_scores.sort(key=lambda x: x['score'], reverse=True)

    # If results are fewer than limit, backfill with popular
    if len(blended_scores) < limit:
        used_ids = set(item['book'].id for item in blended_scores).union(exclude_ids)
        backfill = get_popular_trending_books(limit=limit - len(blended_scores), exclude_ids=used_ids)
        blended_scores.extend(backfill)

    return blended_scores[:limit]
