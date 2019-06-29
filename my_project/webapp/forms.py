from django import forms
from webapp.models import Author, Book, Comment


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ['is_deleted']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none is-valid',
                       'placeholder': 'ФИО', 'required': True}),
            'birth_date': forms.DateInput(
                attrs={'class': 'form-control form-control-sm shadow-none'}),
            'death_date': forms.DateInput(
                attrs={'class': 'form-control form-control-sm shadow-none'}),
            'biography': forms.Textarea(
                attrs={'class': 'form-control form-control-sm shadow-none',
                       'placeholder': 'Биография'}),
        }


class BookForm(forms.ModelForm):
    author = forms.ChoiceField

    class Meta:
        model = Book
        exclude = ['is_deleted']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none is-valid',
                       'placeholder': 'Название', 'required': True}),
            'published_year': forms.TextInput(
                attrs={'class': 'form-control form-control-sm shadow-none',
                       'placeholder': 'Год издания'}),
            'file': forms.FileInput(),
            'picture': forms.FileInput(),
            'description': forms.Textarea(
                attrs={'class': 'form-control form-control-sm shadow-none',
                       'placeholder': 'Описание'}),
        }
