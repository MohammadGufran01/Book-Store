import uuid
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, default='book', help_text='Lucide icon name')
    image_url = models.URLField(blank=True, default='')

    class Meta:
        ordering = ['name']
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books:genre_books', kwargs={'slug': self.slug})


class Author(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    bio = models.TextField(blank=True)
    photo_url = models.URLField(blank=True, default='')
    born_year = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Author.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books:author_books', kwargs={'slug': self.slug})


class Book(models.Model):
    FORMAT_CHOICES = [
        ('Paperback', 'Paperback'),
        ('Hardcover', 'Hardcover'),
        ('eBook', 'eBook / Digital'),
        ('Audiobook', 'Audiobook'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=280, unique=True, blank=True)
    isbn = models.CharField(max_length=20, unique=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genres = models.ManyToManyField(Genre, related_name='books')
    synopsis = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)])
    discount_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    stock = models.PositiveIntegerField(default=10)
    format = models.CharField(max_length=20, choices=FORMAT_CHOICES, default='Paperback')
    pages = models.PositiveIntegerField(default=300)
    publisher = models.CharField(max_length=200, default='Global Publishing')
    publication_year = models.PositiveIntegerField(default=2024)
    language = models.CharField(max_length=50, default='English')
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    cover_url = models.URLField(blank=True, default='')
    
    # Flags & Badges
    is_featured = models.BooleanField(default=False)
    is_bestseller = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Book.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        if not self.isbn:
            self.isbn = f"978-{uuid.uuid4().int % 10000000000:010d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:book_detail', kwargs={'slug': self.slug})

    @property
    def effective_price(self):
        if self.discount_price and self.discount_price > 0 and self.discount_price < self.price:
            return self.discount_price
        return self.price

    @property
    def discount_percentage(self):
        if self.discount_price and self.discount_price < self.price:
            percent = ((self.price - self.discount_price) / self.price) * 100
            return round(percent)
        return 0

    @property
    def in_stock(self):
        return self.stock > 0

    @property
    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            avg = sum(r.rating for r in reviews) / reviews.count()
            return round(avg, 1)
        return 0.0

    @property
    def review_count(self):
        return self.reviews.count()

    def get_cover_image_url(self):
        if self.cover_image:
            return self.cover_image.url
        if self.cover_url:
            return self.cover_url
        return 'https://images.unsplash.com/photo-1544947950-fa07a98d237f?auto=format&fit=crop&q=80&w=600'


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_reviews')
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    headline = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    is_verified_purchase = models.BooleanField(default=False)
    helpful_votes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('book', 'user')

    def __str__(self):
        return f"{self.user.username}'s {self.rating}★ review on {self.book.title}"


class BookInteraction(models.Model):
    """
    Records explicit and implicit interactions for the recommendation engine
    Types: view (weight=1), wishlist (weight=2), cart (weight=3), purchase (weight=5), rate (weight=rating)
    """
    INTERACTION_TYPES = [
        ('view', 'Viewed Book'),
        ('wishlist', 'Added to Wishlist'),
        ('cart', 'Added to Cart'),
        ('purchase', 'Purchased'),
        ('rate', 'Rated'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='interactions')
    session_key = models.CharField(max_length=50, blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='interactions')
    interaction_type = models.CharField(max_length=20, choices=INTERACTION_TYPES, default='view')
    score = models.FloatField(default=1.0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'book']),
            models.Index(fields=['interaction_type']),
        ]

    def __str__(self):
        user_ident = self.user.username if self.user else f"Guest ({self.session_key[:8] if self.session_key else 'anon'})"
        return f"{user_ident} -> {self.interaction_type} on {self.book.title}"

