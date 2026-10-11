from .content_based import get_content_based_similar_books, get_content_based_user_recommendations
from .collaborative import get_user_collaborative_recommendations, get_item_collaborative_similar_books
from .hybrid import get_hybrid_recommendations_for_user, get_popular_trending_books, get_cold_start_recommendations
from .association import get_frequently_bought_together
from books.models import Book, Genre


class RecommendationEngine:
    @staticmethod
    def get_for_user(user, limit=8, exclude_ids=None):
        """
        Returns personalized hybrid recommendations for the logged-in user or bestsellers for guests.
        """
        return get_hybrid_recommendations_for_user(user, limit=limit, exclude_ids=exclude_ids)

    @staticmethod
    def get_similar_books(book, limit=6, exclude_ids=None):
        """
        Returns similar books combining TF-IDF content similarity and item-collaborative patterns.
        """
        if exclude_ids is None:
            exclude_ids = set()

        # 1. Try content-based similarity
        content_sims = get_content_based_similar_books(book, limit=limit, exclude_ids=exclude_ids)
        if len(content_sims) >= limit:
            return content_sims

        # 2. Backfill with item collaborative or genre matches
        seen_ids = set(x['book'].id for x in content_sims).union(exclude_ids)
        collab_sims = get_item_collaborative_similar_books(book, limit=limit - len(content_sims), exclude_ids=seen_ids)
        combined = content_sims + collab_sims

        if len(combined) < limit:
            seen_ids = set(x['book'].id for x in combined).union(exclude_ids)
            genre_fallback = Book.objects.filter(
                is_active=True,
                genres__in=book.genres.all()
            ).exclude(id__in=seen_ids).distinct()[:limit - len(combined)]
            
            for b in genre_fallback:
                combined.append({
                    'book': b,
                    'score': 80.0,
                    'reason': f"More in {book.genres.first().name if book.genres.exists() else 'this genre'}",
                    'algorithm': 'Genre-Match'
                })

        return combined[:limit]

    @staticmethod
    def get_frequently_bought_together(book, limit=3, exclude_ids=None):
        """
        Returns books frequently purchased in the same shopping basket.
        """
        results = get_frequently_bought_together(book, limit=limit, exclude_ids=exclude_ids)
        if not results:
            # Fallback to top 2 similar books from the same genre
            similar = get_content_based_similar_books(book, limit=limit, exclude_ids=exclude_ids)
            for item in similar:
                item['confidence'] = 75
                item['reason'] = f"Great companion to '{book.title}'"
            return similar
        return results

    @staticmethod
    def get_trending_bestsellers(limit=8, exclude_ids=None):
        """
        Returns highest Bayesian-rated bestselling titles.
        """
        return get_popular_trending_books(limit=limit, exclude_ids=exclude_ids)

    @staticmethod
    def get_genre_highlights(genre, limit=6, exclude_ids=None):
        """
        Returns top books within a specific genre.
        """
        if exclude_ids is None:
            exclude_ids = set()

        books = Book.objects.filter(
            is_active=True,
            genres=genre
        ).exclude(id__in=exclude_ids).order_by('-is_bestseller', '-created_at')[:limit]

        return [{
            'book': b,
            'score': 92.0,
            'reason': f"Popular in {genre.name}",
            'algorithm': 'Genre Spotlight'
        } for b in books]
