from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from books.models import Genre, Author


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'alex@example.com'}))
    first_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Alex'}))
    last_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Smith'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Choose username'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-input'


class UserProfileForm(forms.ModelForm):
    favorite_genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'genre-checkbox'}),
        required=False,
        help_text='Select your favorite genres to receive personalized smart book suggestions.'
    )

    class Meta:
        model = UserProfile
        fields = [
            'phone_number', 'bio', 'avatar_url',
            'address_line1', 'address_line2', 'city', 'state', 'postal_code', 'country',
            'reading_goal', 'favorite_genres'
        ]
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '+1 (555) 000-0000'}),
            'bio': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'Tell us about your reading interests...'}),
            'avatar_url': forms.URLInput(attrs={'class': 'form-input', 'placeholder': 'Image URL'}),
            'address_line1': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Street Address'}),
            'address_line2': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Apt / Suite'}),
            'city': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'State'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'ZIP Code'}),
            'country': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Country'}),
            'reading_goal': forms.NumberInput(attrs={'class': 'form-input', 'min': 1, 'max': 100}),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
        }
