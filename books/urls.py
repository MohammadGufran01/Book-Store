from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/<slug:slug>/', views.book_detail, name='book_detail'),
    path('books/<slug:slug>/review/', views.add_review, name='add_review'),
    path('genres/<slug:slug>/', views.genre_books, name='genre_books'),
    path('authors/<slug:slug>/', views.author_books, name='author_books'),
    path('reviews/<int:review_id>/vote/', views.vote_review, name='vote_review'),
    path('api/search-autocomplete/', views.search_autocomplete, name='search_autocomplete'),
]
