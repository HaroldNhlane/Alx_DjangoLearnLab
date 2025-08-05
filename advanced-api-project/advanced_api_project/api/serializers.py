# api/serializers.py

from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    A serializer for the Book model.
    It handles serialization for the title and publication_year fields.
    It also includes a custom validation method to ensure the publication_year
    is not a future date.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year']

    def validate_publication_year(self, value):
        """
        Custom validation to ensure the publication year is not in the future.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    A serializer for the Author model.
    It serializes the author's name and includes a nested representation of all
    their related books using the BookSerializer.
    The `books` field is defined using the `related_name` we set in the model.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']