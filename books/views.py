import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q, Avg, Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Book, Genre, Author, Review, BookInteraction
from .forms import ReviewForm
from recommendations.services.engine import RecommendationEngine
from orders.models import OrderItem

logger = logging.getLogger(__name__)


def home(request):
    """
    Store homepage featuring personalized recommendations, trending titles,
    genre highlights, new arrivals, and featured collections.
    """
    featured_books = Book.objects.filter(is_active=True, is_featured=True).prefetch_related('genres', 'author')[:6]
    new_arrivals = Book.objects.filter(is_active=True).prefetch_related('genres', 'author').order_by('-created_at')[:8]
    bestsellers = Book.objects.filter(is_active=True, is_bestseller=True).prefetch_related('genres', 'author')[:8]
    
    # Recommendation engine feeds
    personalized_recs = RecommendationEngine.get_for_user(request.user, limit=8)
    trending_recs = RecommendationEngine.get_trending_bestsellers(limit=8)
    genres = Genre.objects.all()[:12]

    context = {
        'featured_books': featured_books,
        'new_arrivals': new_arrivals,
        'bestsellers': bestsellers,
        'personalized_recs': personalized_recs,
        'trending_recs': trending_recs,
        'genres': genres,
        'is_home': True,
    }
    return render(request, 'books/home.html', context)


def book_list(request):
    """
    Catalog view supporting keyword search, genre filtering, price range,
    minimum star rating, format filtering, and multiple sorting criteria.
    """
    books = Book.objects.filter(is_active=True).prefetch_related('genres', 'author').annotate(
        avg_rating=Avg('reviews__rating'),
        num_reviews=Count('reviews')
    )

    query = request.GET.get('q', '').strip()
    genre_slug = request.GET.get('genre', '').strip()
    format_type = request.GET.get('format', '').strip()
    min_price = request.GET.get('min_price', '').strip()
    max_price = request.GET.get('max_price', '').strip()
    rating_filter = request.GET.get('rating', '').strip()
    sort_by = request.GET.get('sort', 'popular').strip()

    selected_genre = None
    if genre_slug:
        selected_genre = get_object_or_404(Genre, slug=genre_slug)
        books = books.filter(genres=selected_genre)

    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(author__name__icontains=query) |
            Q(synopsis__icontains=query) |
            Q(isbn__icontains=query) |
            Q(genres__name__icontains=query)
        ).distinct()

    if format_type:
        books = books.filter(format=format_type)

    if min_price:
        try:
            books = books.filter(price__gte=float(min_price))
        except ValueError:
            pass

    if max_price:
        try:
            books = books.filter(price__lte=float(max_price))
        except ValueError:
            pass

    if rating_filter:
        try:
            r_val = float(rating_filter)
            books = books.filter(avg_rating__gte=r_val)
        except ValueError:
            pass

    # Sorting
    if sort_by == 'price_asc':
        books = books.order_by('price')
    elif sort_by == 'price_desc':
        books = books.order_by('-price')
    elif sort_by == 'rating':
        books = books.order_by('-avg_rating', '-num_reviews')
    elif sort_by == 'newest':
        books = books.order_by('-created_at')
    elif sort_by == 'title':
        books = books.order_by('title')
    else:  # popular default
        books = books.order_by('-is_bestseller', '-avg_rating', '-created_at')

    # Pagination: 12 books per page
    paginator = Paginator(books, 12)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    genres = Genre.objects.all()

    context = {
        'books': page_obj,
        'page_obj': page_obj,
        'genres': genres,
        'selected_genre': selected_genre,
        'query': query,
        'format_type': format_type,
        'min_price': min_price,
        'max_price': max_price,
        'rating_filter': rating_filter,
        'sort_by': sort_by,
        'total_count': paginator.count,
    }
    return render(request, 'books/book_list.html', context)


def book_detail(request, slug):
    """
    Single book page with detailed metadata, content-based & collaborative recommendations,
    frequently bought together bundles, verified reviews, and interactive review submission.
    """
    book = get_object_or_404(Book.objects.prefetch_related('genres', 'author', 'reviews__user'), slug=slug, is_active=True)

    # Log interaction for recommendation analytics and implicit collaborative filtering
    try:
        session_key = request.session.session_key or ''
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        
        BookInteraction.objects.create(
            user=request.user if request.user.is_authenticated else None,
            session_key=session_key,
            book=book,
            interaction_type='view',
            score=1.0
        )
    except Exception as e:
        logger.warning(f"Failed to record book interaction: {e}")

    # Recommendations
    similar_books = RecommendationEngine.get_similar_books(book, limit=6)
    frequently_bought = RecommendationEngine.get_frequently_bought_together(book, limit=2)
    
    # Calculate bundle total
    bundle_books = [book] + [item['book'] for item in frequently_bought]
    bundle_total = sum(b.effective_price for b in bundle_books)
    bundle_original = sum(b.price for b in bundle_books)

    # Check if user already reviewed or purchased
    user_has_reviewed = False
    user_review = None
    is_verified_buyer = False

    if request.user.is_authenticated:
        user_review = Review.objects.filter(book=book, user=request.user).first()
        user_has_reviewed = user_review is not None
        is_verified_buyer = OrderItem.objects.filter(
            order__user=request.user,
            book=book,
            order__status__in=['Processing', 'Shipped', 'Delivered']
        ).exists()

    reviews = book.reviews.all().order_by('-created_at')
    review_form = ReviewForm()

    context = {
        'book': book,
        'similar_books': similar_books,
        'frequently_bought': frequently_bought,
        'bundle_books': bundle_books,
        'bundle_total': bundle_total,
        'bundle_original': bundle_original,
        'reviews': reviews,
        'user_has_reviewed': user_has_reviewed,
        'user_review': user_review,
        'is_verified_buyer': is_verified_buyer,
        'review_form': review_form,
    }
    return render(request, 'books/book_detail.html', context)


def genre_books(request, slug):
    """Filter catalog by genre slug directly"""
    genre = get_object_or_404(Genre, slug=slug)
    return redirect(f"/books/?genre={genre.slug}")


def author_books(request, slug):
    """Filter catalog by author"""
    author = get_object_or_404(Author, slug=slug)
    books = Book.objects.filter(author=author, is_active=True).prefetch_related('genres')
    
    paginator = Paginator(books, 12)
    page_obj = paginator.get_page(request.GET.get('page', 1))

    context = {
        'author': author,
        'books': page_obj,
        'page_obj': page_obj,
        'total_count': paginator.count,
    }
    return render(request, 'books/author_detail.html', context)


@login_required
@require_POST
def add_review(request, slug):
    """Submit a rating and review for a book"""
    book = get_object_or_404(Book, slug=slug, is_active=True)
    
    # Check if user already reviewed
    existing_review = Review.objects.filter(book=book, user=request.user).first()
    
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data.get('rating')
        if not rating or rating < 1 or rating > 5:
            messages.error(request, "Please choose a star rating between 1 and 5.")
            return redirect('books:book_detail', slug=book.slug)

        is_verified = OrderItem.objects.filter(
            order__user=request.user,
            book=book,
            order__status__in=['Processing', 'Shipped', 'Delivered']
        ).exists()

        if existing_review:
            existing_review.rating = rating
            existing_review.headline = form.cleaned_data.get('headline')
            existing_review.body = form.cleaned_data.get('body')
            existing_review.is_verified_purchase = is_verified
            existing_review.save()
            messages.success(request, "Your review has been updated successfully!")
        else:
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.is_verified_purchase = is_verified
            review.save()
            
            # Log interaction for recommendation matrix
            BookInteraction.objects.create(
                user=request.user,
                book=book,
                interaction_type='rate',
                score=float(rating)
            )
            messages.success(request, "Thank you for reviewing this book!")
    else:
        messages.error(request, "There was an issue with your review submission. Please check the fields.")

    return redirect('books:book_detail', slug=book.slug)


@login_required
@require_POST
def vote_review(request, review_id):
    """Helpful vote on a review"""
    review = get_object_or_404(Review, id=review_id)
    review.helpful_votes += 1
    review.save(update_fields=['helpful_votes'])
    return JsonResponse({'status': 'success', 'helpful_votes': review.helpful_votes})


def search_autocomplete(request):
    """
    Live autocomplete search API endpoint returning titles, authors, and covers.
    """
    query = request.GET.get('q', '').strip()
    if len(query) < 2:
        return JsonResponse({'results': []})

    books = Book.objects.filter(
        Q(title__icontains=query) |
        Q(author__name__icontains=query) |
        Q(genres__name__icontains=query)
    ).filter(is_active=True).distinct()[:6]

    results = []
    for b in books:
        results.append({
            'id': b.id,
            'title': b.title,
            'author': b.author.name,
            'price': str(b.effective_price),
            'rating': b.average_rating,
            'cover_url': b.get_cover_image_url(),
            'url': b.get_absolute_url(),
        })

    return JsonResponse({'results': results})
