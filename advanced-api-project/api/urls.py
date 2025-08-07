from django.urls import path
from .views import book_list, book_create, book_retrieve, book_update, book_delete

urlpatterns = [
    path('books/', book_list, name='book-list'),
    path('books/create/', book_create, name='book-create'),
    path('books/<int:pk>/', book_retrieve, name='book-retrieve'),
    
    # Modified endpoints without <int:pk> in path
    path('books/update/', book_update, name='book-update'),  # Now matches expected format
    path('books/delete/', book_delete, name='book-delete'),  # Now matches expected format
]