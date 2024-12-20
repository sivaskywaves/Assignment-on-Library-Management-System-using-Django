from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'year', 'genre')

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        author = cleaned_data.get('author')
        year = cleaned_data.get('year')
        genre = cleaned_data.get('genre')

        if not all([title, author, year, genre]):
            raise forms.ValidationError('All fields are required.')

