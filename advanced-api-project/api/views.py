# api/views.py

from rest_framework import generics
from rest_framework import permissions
from .models import Book
from .serializers import BookSerializer

# This view handles listing all books and creating a new book.
# We'll restrict creation to authenticated users only.
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # The IsAuthenticatedOrReadOnly permission class allows anyone to read (GET)
    # but only authenticated users to create (POST).

# This view handles retrieving, updating, and deleting a single book.
# We'll restrict updating and deleting to authenticated users only.
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # This permission class works the same way here: read-only for anyone,
    # but update (PUT/PATCH) and delete (DELETE) only for authenticated users.
