# api/serializers.py

from rest_framework import serializers
from .models import Book, Author
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    It includes a custom validation method to ensure the publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Custom validation method for the 'publication_year' field.
        It checks if the provided year is in the future.
        """
        current_year = timezone.now().year
        if value > current_year:
            # If the year is in the future, raise a validation error.
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    It demonstrates a nested relationship by including a list of related books.
    """
    # The 'books' field uses a nested BookSerializer to handle the one-to-many
    # relationship. 'many=True' is used because an author can have multiple books.
    # 'read_only=True' prevents users from creating/updating books directly through
    # the AuthorSerializer.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']