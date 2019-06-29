from django import forms
from webapp.models import Author


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
