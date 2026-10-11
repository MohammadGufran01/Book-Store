from decimal import Decimal
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from books.models import Genre, Author, Book
from cart.models import Cart, CartItem, Coupon, Wishlist


class CartAndWishlistTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='carttester', password='password123')
        
        self.author = Author.objects.create(name='Test Author')
        self.book1 = Book.objects.create(title='Book Alpha', author=self.author, price=Decimal('300.00'), stock=5, synopsis='Synopsis 1')
        self.book2 = Book.objects.create(title='Book Beta', author=self.author, price=Decimal('400.00'), stock=10, synopsis='Synopsis 2')
        
        self.coupon = Coupon.objects.create(code='TEST10', discount_percent=10, active=True)

    def test_add_to_cart_and_totals(self):
        self.client.login(username='carttester', password='password123')
        
        # Add Book 1 (2 * 300 = 600 >= 499)
        response = self.client.post(reverse('cart:add_to_cart', args=[self.book1.id]), {'quantity': 2})
        self.assertEqual(response.status_code, 302)

        cart = Cart.objects.get(user=self.user)
        self.assertEqual(cart.total_items, 2)
        self.assertEqual(cart.subtotal, Decimal('600.00'))
        
        # Free shipping threshold >= ₹499
        self.assertEqual(cart.shipping_cost, Decimal('0.00'))

    def test_coupon_discount(self):
        self.client.login(username='carttester', password='password123')
        self.client.post(reverse('cart:add_to_cart', args=[self.book1.id]), {'quantity': 1})
        
        # Apply coupon TEST10 (10% off on 300 = 30.00)
        self.client.post(reverse('cart:apply_coupon'), {'code': 'TEST10'})
        
        cart = Cart.objects.get(user=self.user)
        self.assertEqual(cart.coupon, self.coupon)
        self.assertEqual(cart.discount, Decimal('30.00'))

    def test_wishlist_toggle(self):
        self.client.login(username='carttester', password='password123')
        
        # Add to wishlist
        response = self.client.post(reverse('cart:toggle_wishlist', args=[self.book1.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Wishlist.objects.filter(user=self.user, book=self.book1).exists())

        # Remove from wishlist
        self.client.post(reverse('cart:toggle_wishlist', args=[self.book1.id]))
        self.assertFalse(Wishlist.objects.filter(user=self.user, book=self.book1).exists())
