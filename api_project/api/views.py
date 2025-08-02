# api_project/api/views.py

from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# This is the view for your original 'books/' endpoint
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# This is the new ViewSet for all CRUD operations at 'books_all/'
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer