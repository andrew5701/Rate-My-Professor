from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['heading', 'review', 'rating', 'courses']

        # widgets = {
        #     'review': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': "Write a review"
        #     })
        # }
