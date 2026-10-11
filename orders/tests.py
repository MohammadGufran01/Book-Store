from decimal import Decimal
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from books.models import Author, Book
from cart.models import Cart, CartItem
from orders.models import Order, OrderItem


class OrderAndCheckoutTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='ordertester', password='password123', email='buyer@example.com')
        
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(title='Order Book', author=self.author, price=Decimal('25.00'), stock=10, synopsis='A test book synopsis')
        
        self.cart = Cart.objects.create(user=self.user)
        self.cart_item = CartItem.objects.create(cart=self.cart, book=self.book, quantity=2)

    def test_checkout_and_order_creation(self):
        self.client.login(username='ordertester', password='password123')
        
        checkout_data = {
            'full_name': 'Order Tester',
            'email': 'buyer@example.com',
            'phone': '555-123-4567',
            'country': 'United States',
            'address_line1': '100 Main Street',
            'city': 'Metropolis',
            'state': 'NY',
            'postal_code': '10001',
            'payment_method': 'credit_card',
        }
        
        response = self.client.post(reverse('orders:checkout'), checkout_data)
        self.assertEqual(response.status_code, 302)
        
        # Verify order created
        order = Order.objects.filter(user=self.user).first()
        self.assertIsNotNone(order)
        self.assertEqual(order.full_name, 'Order Tester')
        self.assertEqual(order.subtotal, Decimal('50.00'))
        self.assertEqual(order.items.count(), 1)
        
        # Verify stock decremented (10 - 2 = 8)
        self.book.refresh_from_db()
        self.assertEqual(self.book.stock, 8)
        
        # Verify cart was cleared
        self.cart.refresh_from_db()
        self.assertEqual(self.cart.items.count(), 0)
