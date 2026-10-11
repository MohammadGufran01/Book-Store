from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import UserRegisterForm, UserProfileForm, UserUpdateForm
from .models import UserProfile
from recommendations.services.engine import RecommendationEngine
from cart.models import Cart
from books.models import Review
from orders.models import Order


def register_view(request):
    """Register new user with automatic profile initialization and immediate login"""
    if request.user.is_authenticated:
        return redirect('books:home')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Migrate guest cart if exists
            session_key = request.session.session_key
            if session_key:
                guest_cart = Cart.objects.filter(session_key=session_key).first()
                if guest_cart:
                    guest_cart.user = user
                    guest_cart.save()
            
            login(request, user)
            messages.success(request, f"Welcome to Reader's Haven, {user.username}! Your account is ready.")
            return redirect('accounts:profile')
        else:
            messages.error(request, "Registration failed. Please check the errors below.")
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('books:home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                
                # Migrate guest session cart to user cart
                session_key = request.session.session_key
                if session_key:
                    guest_cart = Cart.objects.filter(session_key=session_key).first()
                    if guest_cart:
                        user_cart, _ = Cart.objects.get_or_create(user=user)
                        # Merge items
                        for g_item in guest_cart.items.all():
                            u_item, created = user_cart.items.get_or_create(book=g_item.book)
                            if not created:
                                u_item.quantity += g_item.quantity
                            else:
                                u_item.quantity = g_item.quantity
                            u_item.save()
                        guest_cart.delete()

                messages.success(request, f"Welcome back, {user.username}!")
                next_url = request.GET.get('next') or 'books:home'
                return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    # Pre-fetch demo test accounts for easy one-click testing
    demo_users = User.objects.filter(is_superuser=False)[:4]

    return render(request, 'accounts/login.html', {
        'form': form,
        'demo_users': demo_users
    })


def logout_view(request):
    """Logout current user"""
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('books:home')


def demo_login(request, username):
    """One-click demo login for rapid testing of recommendations"""
    user = User.objects.filter(username=username).first()
    if user:
        login(request, user)
        messages.success(request, f"Logged in as demo persona: {user.username}")
    else:
        messages.error(request, f"Demo user '{username}' not found. Please seed the database first.")
    return redirect('books:home')


@login_required
def profile_view(request):
    """User profile management, reading preferences onboarding, and reading tracker"""
    profile, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile and reading preferences have been saved!")
            return redirect('accounts:profile')
        else:
            messages.error(request, "Please correct the errors in the profile form.")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=profile)

    # Reading Stats
    recent_orders = Order.objects.filter(user=request.user).order_by('-created_at')[:3]
    recent_reviews = Review.objects.filter(user=request.user).select_related('book').order_by('-created_at')[:4]
    personalized_recs = RecommendationEngine.get_for_user(request.user, limit=6)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile,
        'recent_orders': recent_orders,
        'recent_reviews': recent_reviews,
        'personalized_recs': personalized_recs,
    }
    return render(request, 'accounts/profile.html', context)
