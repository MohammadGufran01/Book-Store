import logging
from collections import defaultdict
from orders.models import OrderItem, Order
from books.models import Book

logger = logging.getLogger(__name__)


def get_frequently_bought_together(target_book, limit=3, exclude_ids=None):
    """
    Market Basket Co-occurrence Analysis:
    Identifies books that most frequently appear in the same order as the target book.
    """
    if exclude_ids is None:
        exclude_ids = set()
    exclude_ids.add(target_book.id)

    try:
        # Find order IDs containing target_book
        order_ids = OrderItem.objects.filter(
            book=target_book,
            order__status__in=['Processing', 'Shipped', 'Delivered', 'Pending']
        ).values_list('order_id', flat=True)

        if not order_ids:
            return []

        # Count co-occurrences of other books in these orders
        co_items = OrderItem.objects.filter(
            order_id__in=order_ids
        ).exclude(book_id__in=exclude_ids).values('book_id')

        co_counts = defaultdict(int)
        for item in co_items:
            b_id = item['book_id']
            if b_id:
                co_counts[b_id] += 1

        if not co_counts:
            return []

        # Sort by co-occurrence frequency
        sorted_pairs = sorted(co_counts.items(), key=lambda x: x[1], reverse=True)[:limit]
        candidate_ids = [b_id for b_id, _ in sorted_pairs]

        book_objects = {b.id: b for b in Book.objects.filter(id__in=candidate_ids, is_active=True).prefetch_related('genres', 'author')}

        results = []
        for b_id, freq in sorted_pairs:
            if b_id in book_objects:
                confidence = round((freq / len(order_ids)) * 100)
                results.append({
                    'book': book_objects[b_id],
                    'frequency': freq,
                    'confidence': confidence,
                    'reason': f"Frequently bought together with '{target_book.title}'",
                    'algorithm': 'Market Basket Association'
                })

        return results
    except Exception as e:
        logger.error(f"Association rule mining error: {e}")
        return []
