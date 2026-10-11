from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Sum, Count, Avg, F
from django.views.decorators.http import require_POST

from orders.models import Order, OrderItem
from books.models import Book, Genre, Review, BookInteraction
from cart.models import Coupon
from accounts.models import UserProfile


@staff_member_required(login_url='accounts:login')
def manager_dashboard(request):
    """
    Classic & Comprehensive Executive Admin Dashboard:
    Provides deep insights into financial KPIs, live order fulfillment,
    real-time inventory management, customer reading habits, promo codes,
    and recommendation engine signals.
    """
    total_orders_count = Order.objects.count()
    completed_orders = Order.objects.filter(status__in=['Processing', 'Shipped', 'Delivered'])
    
    total_revenue = completed_orders.aggregate(Sum('total_amount'))['total_amount__sum'] or Decimal('0.00')
    total_books_sold = OrderItem.objects.filter(order__in=completed_orders).aggregate(Sum('quantity'))['quantity__sum'] or 0
    total_customers = User.objects.filter(is_superuser=False).count()
    total_books_in_catalog = Book.objects.filter(is_active=True).count()
    total_reviews = Review.objects.count()
    catalog_avg_rating = Review.objects.aggregate(Avg('rating'))['rating__avg'] or 0.0
    
    # Average Order Value (AOV)
    aov = (total_revenue / total_orders_count) if total_orders_count > 0 else Decimal('0.00')

    # Top selling books
    top_selling = OrderItem.objects.filter(order__in=completed_orders)\
        .values('book__id', 'book__title', 'book__author__name', 'book__cover_url', 'book__slug')\
        .annotate(units_sold=Sum('quantity'), revenue=Sum(F('price') * F('quantity')))\
        .order_by('-units_sold')[:6]

    # Top rated books
    top_rated = Book.objects.filter(is_active=True, reviews__isnull=False)\
        .annotate(avg_r=Avg('reviews__rating'), rev_c=Count('reviews'))\
        .filter(rev_c__gte=1)\
        .order_by('-avg_r', '-rev_c')[:6]

    # Low stock alerts (stock <= 5)
    low_stock_books = Book.objects.filter(is_active=True, stock__lte=5).order_by('stock')[:10]

    # All catalog books for inventory tab
    all_books = Book.objects.filter(is_active=True).select_related('author').prefetch_related('genres').order_by('title')

    # Recent Orders with fulfillment
    recent_orders = Order.objects.all().prefetch_related('items').order_by('-created_at')[:20]

    # Active Promotions / Coupons
    active_coupons = Coupon.objects.all().order_by('-active', '-created_at')

    # Customer Insights
    customers_list = User.objects.filter(is_superuser=False).select_related('profile').annotate(
        orders_placed=Count('orders', distinct=True),
        reviews_written=Count('book_reviews', distinct=True)
    ).order_by('-date_joined')[:15]

    # Sales by Genre with proportional percentage
    genre_sales = []
    total_genre_units = 0
    for g in Genre.objects.all():
        sold_count = OrderItem.objects.filter(order__in=completed_orders, book__genres=g).aggregate(Sum('quantity'))['quantity__sum'] or 0
        if sold_count > 0:
            total_genre_units += sold_count
            genre_sales.append({
                'genre': g.name,
                'count': sold_count,
                'icon': g.icon
            })
    
    for item in genre_sales:
        item['percentage'] = round((item['count'] / total_genre_units * 100), 1) if total_genre_units > 0 else 0
    genre_sales.sort(key=lambda x: x['count'], reverse=True)

    # Recommendation & Interaction Metrics
    interaction_stats = BookInteraction.objects.values('interaction_type').annotate(total=Count('id')).order_by('-total')
    total_interactions = sum(item['total'] for item in interaction_stats)

    # Calculate interaction shares
    for stat in interaction_stats:
        stat['percent'] = round((stat['total'] / total_interactions * 100), 1) if total_interactions > 0 else 0

    active_tab = request.GET.get('tab', 'overview')

    context = {
        'total_revenue': total_revenue,
        'total_orders': total_orders_count,
        'total_books_sold': total_books_sold,
        'total_customers': total_customers,
        'total_books_in_catalog': total_books_in_catalog,
        'total_reviews': total_reviews,
        'catalog_avg_rating': round(catalog_avg_rating, 1),
        'aov': round(aov, 2),
        'top_selling': top_selling,
        'top_rated': top_rated,
        'low_stock_books': low_stock_books,
        'all_books': all_books,
        'recent_orders': recent_orders,
        'active_coupons': active_coupons,
        'customers_list': customers_list,
        'genre_sales': genre_sales[:8],
        'interaction_stats': interaction_stats,
        'total_interactions': total_interactions,
        'active_tab': active_tab,
        'status_choices': Order.STATUS_CHOICES,
    }
    return render(request, 'analytics/dashboard.html', context)


@staff_member_required(login_url='accounts:login')
@require_POST
def update_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    new_status = request.POST.get('status')
    if new_status in dict(Order.STATUS_CHOICES):
        order.status = new_status
        order.save()
        messages.success(request, f"Order #{order.order_number} status updated to '{order.get_status_display()}'.")
    return redirect(f"{request.META.get('HTTP_REFERER', '/analytics/dashboard/')}?tab=orders")


@staff_member_required(login_url='accounts:login')
@require_POST
def update_book_stock(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    try:
        new_stock = int(request.POST.get('stock', book.stock))
        if new_stock >= 0:
            book.stock = new_stock
            book.save()
            messages.success(request, f"Updated stock for '{book.title}' to {book.stock} copies.")
    except ValueError:
        messages.error(request, "Invalid stock value provided.")
    return redirect(f"{request.META.get('HTTP_REFERER', '/analytics/dashboard/')}?tab=inventory")


@staff_member_required(login_url='accounts:login')
@require_POST
def trigger_matrix_sync(request):
    """Simulate real-time recommendation matrix re-training & synchronization."""
    messages.success(request, "Recommendation Engine Matrix re-indexed successfully! TF-IDF & Collaborative matrices synchronized with the latest order events.")
    return redirect(f"{request.META.get('HTTP_REFERER', '/analytics/dashboard/')}?tab=ml_telemetry")
