import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.views.decorators.http import require_POST

from .models import Order, OrderItem
from .forms import CheckoutForm
from cart.models import Cart
from cart.context_processors import get_or_create_cart
from books.models import Book, BookInteraction

logger = logging.getLogger(__name__)


def checkout(request):
    """
    Checkout view: gathers shipping info, calculates final amounts,
    simulates payment, creates order & order items, and updates stock & user interactions.
    """
    cart = get_or_create_cart(request)
    cart_items = cart.items.select_related('book').all()

    if not cart_items.exists():
        messages.warning(request, "Your cart is empty. Add some books before checking out!")
        return redirect('books:book_list')

    # Pre-populate form with user profile details if logged in
    initial_data = {}
    if request.user.is_authenticated:
        profile = getattr(request.user, 'profile', None)
        initial_data = {
            'full_name': f"{request.user.first_name} {request.user.last_name}".strip() or request.user.username,
            'email': request.user.email,
            'phone': profile.phone_number if profile else '',
            'address_line1': profile.address_line1 if profile else '',
            'address_line2': profile.address_line2 if profile else '',
            'city': profile.city if profile else '',
            'state': profile.state if profile else '',
            'postal_code': profile.postal_code if profile else '',
            'country': profile.country if profile and profile.country else 'United States',
        }

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    order = form.save(commit=False)
                    if request.user.is_authenticated:
                        order.user = request.user
                    
                    # Store financial snapshots
                    order.subtotal = cart.subtotal
                    order.discount_amount = cart.discount
                    order.shipping_fee = cart.shipping_cost
                    order.tax_amount = cart.estimated_tax
                    order.total_amount = cart.total
                    order.coupon_code = cart.coupon.code if cart.coupon else ''
                    
                    # Payment simulation
                    payment_method = form.cleaned_data.get('payment_method')
                    if payment_method == 'cod':
                        order.payment_status = 'Pending'
                        order.status = 'Processing'
                    else:
                        order.payment_status = 'Paid'
                        order.status = 'Processing'
                    
                    order.save()

                    # Create order items and update stock & interactions
                    for item in cart_items:
                        OrderItem.objects.create(
                            order=order,
                            book=item.book,
                            book_title=item.book.title,
                            book_author=item.book.author.name,
                            price=item.unit_price,
                            quantity=item.quantity
                        )
                        
                        # Decrement book stock
                        item.book.stock = max(0, item.book.stock - item.quantity)
                        item.book.save(update_fields=['stock'])

                        # Log purchase interaction for ML Collaborative Filtering
                        if request.user.is_authenticated:
                            BookInteraction.objects.create(
                                user=request.user,
                                book=item.book,
                                interaction_type='purchase',
                                score=5.0
                            )

                    # Clear cart items and coupon
                    cart.items.all().delete()
                    cart.coupon = None
                    cart.save()

                    messages.success(request, f"Order #{order.order_number} placed successfully!")
                    return redirect('orders:order_success', order_number=order.order_number)

            except Exception as e:
                logger.error(f"Order placement error: {e}")
                messages.error(request, f"Failed to place order: {str(e)}")
        else:
            messages.error(request, "Please correct the errors in the checkout form.")
    else:
        form = CheckoutForm(initial=initial_data)

    context = {
        'cart': cart,
        'cart_items': cart_items,
        'form': form,
    }
    return render(request, 'orders/checkout.html', context)


def order_success(request, order_number):
    """Order confirmation and printable receipt view"""
    order = get_object_or_404(Order.objects.prefetch_related('items__book'), order_number=order_number)
    
    # Restrict viewing if order belongs to another authenticated user
    if order.user and request.user.is_authenticated and order.user != request.user and not request.user.is_staff:
        messages.error(request, "You do not have permission to view this order.")
        return redirect('books:home')

    context = {
        'order': order,
        'items': order.items.all(),
    }
    return render(request, 'orders/order_success.html', context)


def order_detail(request, order_number):
    """Detailed invoice and order tracking view"""
    order = get_object_or_404(Order.objects.prefetch_related('items__book'), order_number=order_number)

    if order.user and request.user.is_authenticated and order.user != request.user and not request.user.is_staff:
        messages.error(request, "You do not have permission to view this order.")
        return redirect('books:home')

    context = {
        'order': order,
        'items': order.items.all(),
    }
    return render(request, 'orders/order_detail.html', context)


@login_required
def order_history(request):
    """List all orders for logged-in user"""
    orders = Order.objects.filter(user=request.user).prefetch_related('items__book').order_by('-created_at')
    context = {
        'orders': orders,
    }
    return render(request, 'orders/order_history.html', context)


@login_required
@require_POST
def cancel_order(request, order_number):
    """Allow customer to cancel a pending order"""
    order = get_object_or_404(Order, order_number=order_number, user=request.user)
    if order.status in ['Pending', 'Processing']:
        order.status = 'Cancelled'
        order.save(update_fields=['status'])
        
        # Restore stock
        for item in order.items.all():
            if item.book:
                item.book.stock += item.quantity
                item.book.save(update_fields=['stock'])
                
        messages.info(request, f"Order #{order.order_number} has been cancelled.")
    else:
        messages.warning(request, "This order cannot be cancelled as it has already been shipped or processed.")

    return redirect('orders:order_detail', order_number=order.order_number)
