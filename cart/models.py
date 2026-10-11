from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from books.models import Book


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percent = models.PositiveIntegerField(default=0, help_text='Discount percentage (0-100)')
    discount_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0, help_text='Fixed dollar discount')
    min_spend = models.DecimalField(max_digits=8, decimal_places=2, default=0, help_text='Minimum cart subtotal required')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} ({self.discount_percent}% off or ₹{self.discount_amount} off)"

    def calculate_discount(self, subtotal):
        if subtotal < self.min_spend or not self.active:
            return Decimal('0.00')
        
        discount = Decimal('0.00')
        if self.discount_percent > 0:
            discount = (subtotal * Decimal(self.discount_percent)) / Decimal(100)
        elif self.discount_amount > 0:
            discount = min(self.discount_amount, subtotal)
            
        return round(discount, 2)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='carts')
    session_key = models.CharField(max_length=50, blank=True, null=True, db_index=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        ident = self.user.username if self.user else f"Session: {self.session_key}"
        return f"Cart for {ident} ({self.items.count()} items)"

    @property
    def total_items(self):
        return sum(item.quantity for item in self.items.all())

    @property
    def subtotal(self):
        return sum(item.total_price for item in self.items.all())

    @property
    def discount(self):
        if self.coupon:
            return self.coupon.calculate_discount(self.subtotal)
        return Decimal('0.00')

    @property
    def discounted_subtotal(self):
        return max(Decimal('0.00'), self.subtotal - self.discount)

    @property
    def shipping_cost(self):
        if self.subtotal == 0 or self.discounted_subtotal >= Decimal('499.00'):
            return Decimal('0.00')
        return Decimal('49.00')

    @property
    def estimated_tax(self):
        # 5% estimated tax
        return round(self.discounted_subtotal * Decimal('0.05'), 2)

    @property
    def total(self):
        if self.subtotal == 0:
            return Decimal('0.00')
        return round(self.discounted_subtotal + self.shipping_cost + self.estimated_tax, 2)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        unique_together = ('cart', 'book')

    def __str__(self):
        return f"{self.quantity}x {self.book.title}"

    @property
    def unit_price(self):
        return self.book.effective_price

    @property
    def total_price(self):
        return round(self.unit_price * self.quantity, 2)


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist_items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='in_wishlists')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('user', 'book')

    def __str__(self):
        return f"{self.user.username} saved {self.book.title}"
