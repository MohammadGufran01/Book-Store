from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from books.models import Genre, Author


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=20, blank=True)
    avatar_url = models.URLField(blank=True, default='https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=200')
    bio = models.TextField(blank=True)
    
    # Address details
    address_line1 = models.CharField(max_length=255, blank=True)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, default='United States')
    
    # Recommendation preferences (Cold-start onboarding)
    favorite_genres = models.ManyToManyField(Genre, blank=True, related_name='interested_users')
    favorite_authors = models.ManyToManyField(Author, blank=True, related_name='interested_users')
    
    # Reading Gamification
    reading_goal = models.PositiveIntegerField(default=12, help_text='Number of books to read this year')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    @property
    def full_address(self):
        parts = [self.address_line1, self.address_line2, self.city, self.state, self.postal_code, self.country]
        return ", ".join(filter(None, parts))

    @property
    def books_read_count(self):
        # Unique books reviewed or bought by this user
        from orders.models import OrderItem
        from books.models import Review
        purchased_ids = OrderItem.objects.filter(order__user=self.user, order__status__in=['Delivered', 'Processing', 'Shipped']).values_list('book_id', flat=True)
        reviewed_ids = Review.objects.filter(user=self.user).values_list('book_id', flat=True)
        return len(set(list(purchased_ids) + list(reviewed_ids)))

    @property
    def goal_progress_percent(self):
        if self.reading_goal <= 0:
            return 100
        percent = (self.books_read_count / self.reading_goal) * 100
        return min(round(percent), 100)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        if hasattr(instance, 'profile'):
            instance.profile.save()
