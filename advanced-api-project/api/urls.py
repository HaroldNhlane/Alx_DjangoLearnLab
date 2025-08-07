# api/urls.py

from django.urls import path
from .views import book_list, book_create, book_retrieve, book_update, book_delete

urlpatterns = [
    # Separate URLs for each action
    path('books/', book_list, name='book-list'),
    path('books/create/', book_create, name='book-create'),
    path('books/<int:pk>/', book_retrieve, name='book-retrieve'),
    path('books/<int:pk>/update/', book_update, name='book-update'),
    path('books/<int:pk>/delete/', book_delete, name='book-delete'),
]