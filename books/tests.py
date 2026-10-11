from decimal import Decimal
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from books.models import Genre, Author, Book, Review, BookInteraction


class BookCatalogTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testreader', password='password123')
        
        self.genre_scifi = Genre.objects.create(name='Science Fiction')
        self.author_herbert = Author.objects.create(name='Frank Herbert', born_year='1920')
        
        self.book1 = Book.objects.create(
            title='Dune',
            author=self.author_herbert,
            price=Decimal('20.00'),
            discount_price=Decimal('15.00'),
            stock=10,
            synopsis='A desert planet story about spice and power.'
        )
        self.book1.genres.add(self.genre_scifi)

        self.book2 = Book.objects.create(
            title='Dune Messiah',
            author=self.author_herbert,
            price=Decimal('18.00'),
            stock=5,
            synopsis='The continuation of the Arrakis saga.'
        )
        self.book2.genres.add(self.genre_scifi)

    def test_effective_price_and_discount(self):
        self.assertEqual(self.book1.effective_price, Decimal('15.00'))
        self.assertEqual(self.book1.discount_percentage, 25)
        self.assertEqual(self.book2.effective_price, Decimal('18.00'))
        self.assertEqual(self.book2.discount_percentage, 0)

    def test_review_and_average_rating(self):
        self.assertEqual(self.book1.average_rating, 0.0)
        self.assertEqual(self.book1.review_count, 0)

        Review.objects.create(book=self.book1, user=self.user, rating=5, headline='Masterpiece', body='Loved every page!')
        self.assertEqual(self.book1.average_rating, 5.0)
        self.assertEqual(self.book1.review_count, 1)

    def test_home_view(self):
        response = self.client.get(reverse('books:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/home.html')

    def test_book_list_filter_and_search(self):
        # All books
        response = self.client.get(reverse('books:book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['books']), 2)

        # Filter by genre
        response = self.client.get(reverse('books:book_list') + f'?genre={self.genre_scifi.slug}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['books']), 2)

        # Filter by search
        response = self.client.get(reverse('books:book_list') + '?q=Messiah')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['books']), 1)
        self.assertEqual(response.context['books'][0].title, 'Dune Messiah')

    def test_book_detail_view(self):
        response = self.client.get(self.book1.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dune')
        self.assertContains(response, 'Frank Herbert')

    def test_search_autocomplete_api(self):
        response = self.client.get(reverse('books:search_autocomplete') + '?q=Dune')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('results', data)
        self.assertTrue(len(data['results']) >= 2)
