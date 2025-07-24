# relationship_app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Book # Make sure to import your Book model

class UserRegisterForm(UserCreationForm):
    """
    A custom form for user registration.
    Inherits from Django's built-in UserCreationForm.
    """
    class Meta(UserCreationForm.Meta):
        model = UserCreationForm.Meta.model
        fields = UserCreationForm.Meta.fields

# --- Add this BookForm class ---
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn', 'summary'] # Adjust fields to match your Book model fields