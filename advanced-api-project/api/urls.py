# api/urls.py

from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    # This URL maps to the list and create view.
    # It will handle GET (list all books) and POST (create a new book) requests.
    path('books/', BookListCreateView.as_view(), name='book-list-create'),

    # This URL maps to the retrieve, update, and destroy view.
    # The <int:pk> part is a URL parameter that captures the primary key of the book.
    # It will handle GET (retrieve), PUT/PATCH (update), and DELETE (delete) requests.
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),
]