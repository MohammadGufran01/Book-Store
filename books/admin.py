from django.contrib import admin
from .models import Genre, Author, Book, Review, BookInteraction

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'icon')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'born_year')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'bio')

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0
    readonly_fields = ('created_at',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'discount_price', 'stock', 'format', 'is_featured', 'is_bestseller', 'is_active')
    list_filter = ('is_featured', 'is_bestseller', 'is_active', 'format', 'genres')
    search_fields = ('title', 'isbn', 'author__name', 'synopsis')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('genres',)
    inlines = [ReviewInline]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'headline', 'is_verified_purchase', 'created_at')
    list_filter = ('rating', 'is_verified_purchase', 'created_at')
    search_fields = ('book__title', 'user__username', 'headline', 'body')

@admin.register(BookInteraction)
class BookInteractionAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_key', 'book', 'interaction_type', 'score', 'created_at')
    list_filter = ('interaction_type', 'created_at')
    search_fields = ('user__username', 'book__title')
