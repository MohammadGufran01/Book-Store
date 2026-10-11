from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'city', 'country', 'reading_goal', 'created_at')
    search_fields = ('user__username', 'user__email', 'phone_number', 'city')
    filter_horizontal = ('favorite_genres', 'favorite_authors')
