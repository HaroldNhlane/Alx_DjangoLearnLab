# api/urls.py

from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    # This URL handles GET (list) and POST (create) requests
    path('books/', BookListCreateView.as_view(), name='book-list-create'),

    # This URL handles GET (retrieve), PUT/PATCH (update), and DELETE (destroy)
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),
]