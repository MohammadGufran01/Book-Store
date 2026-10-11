from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'headline', 'body']
        widgets = {
            'rating': forms.HiddenInput(),
            'headline': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2.5 rounded-lg border border-slate-300 focus:ring-2 focus:ring-amber-500 focus:border-amber-500 text-sm',
                'placeholder': 'What is the most important thing to know? (e.g., A Masterpiece of World-Building!)'
            }),
            'body': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2.5 rounded-lg border border-slate-300 focus:ring-2 focus:ring-amber-500 focus:border-amber-500 text-sm',
                'rows': 4,
                'placeholder': 'What did you like or dislike? What should other readers know before reading?'
            }),
        }
