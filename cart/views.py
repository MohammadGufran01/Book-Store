import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Cart, CartItem, Coupon, Wishlist
from .context_processors import get_or_create_cart
from books.models import Book, BookInteraction
from recommendations.services.engine import RecommendationEngine

logger = logging.getLogger(__name__)


def cart_detail(request):
    """
    Shopping cart page with subtotal, applied coupon, shipping, tax,
    and personalized cart cross-sell recommendations.
    """
    cart = get_or_create_cart(request)
    cart_items = cart.items.select_related('book', 'book__author').all()

    # Recommendations based on books currently in cart
    recommended_books = []
    if cart_items.exists():
        first_book = cart_items.first().book
        exclude_ids = set(item.book_id for item in cart_items)
        recommended_books = RecommendationEngine.get_similar_books(first_book, limit=4, exclude_ids=exclude_ids)
    else:
        recommended_books = RecommendationEngine.get_trending_bestsellers(limit=4)

    context = {
        'cart': cart,
        'cart_items': cart_items,
        'recommended_books': recommended_books,
    }
    return render(request, 'cart/cart_detail.html', context)


@require_POST
def add_to_cart(request, book_id):
    """Add a book to the shopping cart"""
    book = get_object_or_404(Book, id=book_id, is_active=True)
    cart = get_or_create_cart(request)
    
    quantity = int(request.POST.get('quantity', 1))
    if quantity < 1:
        quantity = 1

    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    
    # Stock limit check
    if cart_item.quantity > book.stock:
        cart_item.quantity = max(1, book.stock)
        messages.warning(request, f"We only have {book.stock} copies of '{book.title}' in stock.")
    else:
        messages.success(request, f"Added '{book.title}' to your cart.")

    cart_item.save()

    # Log interaction
    try:
        BookInteraction.objects.create(
            user=request.user if request.user.is_authenticated else None,
            session_key=request.session.session_key,
            book=book,
            interaction_type='cart',
            score=3.0
        )
    except Exception as e:
        logger.warning(f"Error logging cart interaction: {e}")

    # If buy now clicked, redirect straight to checkout
    if request.POST.get('buy_now') == 'true':
        return redirect('orders:checkout')

    # If AJAX request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.POST.get('format') == 'json':
        return JsonResponse({
            'status': 'success',
            'cart_count': cart.total_items,
            'message': f"Added '{book.title}' to cart."
        })

    next_url = request.POST.get('next') or request.META.get('HTTP_REFERER') or 'cart:cart_detail'
    return redirect(next_url)


@require_POST
def update_cart_item(request, item_id):
    """Increment, decrement, or set quantity of cart item"""
    cart = get_or_create_cart(request)
    cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
    
    action = request.POST.get('action')
    if action == 'increase':
        if cart_item.quantity < cart_item.book.stock:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, "Cart updated.")
        else:
            messages.warning(request, f"Max stock reached ({cart_item.book.stock} available).")
    elif action == 'decrease':
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
            messages.success(request, "Cart updated.")
        else:
            cart_item.delete()
            messages.info(request, f"Removed '{cart_item.book.title}' from your cart.")
    
    return redirect('cart:cart_detail')


@require_POST
def remove_from_cart(request, item_id):
    """Remove item completely from cart"""
    cart = get_or_create_cart(request)
    cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
    book_title = cart_item.book.title
    cart_item.delete()
    messages.info(request, f"Removed '{book_title}' from your cart.")
    return redirect('cart:cart_detail')


@require_POST
def apply_coupon(request):
    """Apply discount coupon code"""
    code = request.POST.get('code', '').strip().upper()
    cart = get_or_create_cart(request)

    if not code:
        messages.error(request, "Please enter a valid promo code.")
        return redirect('cart:cart_detail')

    coupon = Coupon.objects.filter(code=code, active=True).first()
    if not coupon:
        messages.error(request, f"Promo code '{code}' is invalid or has expired.")
        return redirect('cart:cart_detail')

    if cart.subtotal < coupon.min_spend:
        messages.warning(request, f"Promo code '{code}' requires a minimum spend of ${coupon.min_spend}.")
        return redirect('cart:cart_detail')

    cart.coupon = coupon
    cart.save()
    messages.success(request, f"Promo code '{coupon.code}' applied successfully!")
    return redirect('cart:cart_detail')


@require_POST
def remove_coupon(request):
    """Remove applied coupon"""
    cart = get_or_create_cart(request)
    cart.coupon = None
    cart.save()
    messages.info(request, "Promo code removed.")
    return redirect('cart:cart_detail')


@require_POST
def add_bundle_to_cart(request):
    """Adds multiple books in a Frequently Bought Together bundle to cart in one action"""
    book_ids = request.POST.getlist('book_ids')
    cart = get_or_create_cart(request)
    
    added_count = 0
    for b_id in book_ids:
        try:
            book = Book.objects.get(id=int(b_id), is_active=True)
            cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
            if not created:
                cart_item.quantity += 1
            cart_item.save()
            added_count += 1
        except (Book.DoesNotExist, ValueError):
            continue

    if added_count > 0:
        messages.success(request, f"Successfully added {added_count} bundle books to your cart!")
    return redirect('cart:cart_detail')


@login_required
def wishlist(request):
    """View saved wishlist books"""
    items = Wishlist.objects.filter(user=request.user).select_related('book', 'book__author').order_by('-created_at')
    
    # Recommendations based on wishlist
    recs = RecommendationEngine.get_for_user(request.user, limit=4)

    context = {
        'items': items,
        'recommendations': recs,
    }
    return render(request, 'cart/wishlist.html', context)


@login_required
@require_POST
def toggle_wishlist(request, book_id):
    """Toggle book in user's wishlist (AJAX or Redirect)"""
    book = get_object_or_404(Book, id=book_id)
    wishlist_item = Wishlist.objects.filter(user=request.user, book=book).first()

    if wishlist_item:
        wishlist_item.delete()
        in_wishlist = False
        msg = f"Removed '{book.title}' from your wishlist."
    else:
        Wishlist.objects.create(user=request.user, book=book)
        in_wishlist = True
        msg = f"Added '{book.title}' to your wishlist!"
        
        # Log interaction for recommendation matrix
        BookInteraction.objects.create(
            user=request.user,
            book=book,
            interaction_type='wishlist',
            score=3.5
        )

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        wishlist_count = Wishlist.objects.filter(user=request.user).count()
        return JsonResponse({
            'status': 'success',
            'in_wishlist': in_wishlist,
            'wishlist_count': wishlist_count,
            'message': msg
        })

    messages.success(request, msg)
    next_url = request.POST.get('next') or request.META.get('HTTP_REFERER') or 'cart:wishlist'
    return redirect(next_url)


@login_required
@require_POST
def wishlist_to_cart(request, book_id):
    """Move a book from wishlist to cart"""
    book = get_object_or_404(Book, id=book_id)
    cart = get_or_create_cart(request)

    # Add to cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    # Remove from wishlist
    Wishlist.objects.filter(user=request.user, book=book).delete()

    messages.success(request, f"Moved '{book.title}' to your cart!")
    return redirect('cart:wishlist')
