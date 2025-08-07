# api/views.py

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allows read for anyone, write for authenticated
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # Set owner to current user

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Requires authentication for all operations
    
    def get_queryset(self):
        # Optional: Filter to only show user's own books
        return self.queryset.filter(owner=self.request.user)