from django import forms
from .models import Book, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'rating', 'comment']