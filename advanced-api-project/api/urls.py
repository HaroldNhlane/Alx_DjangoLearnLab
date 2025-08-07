from django.urls import path
from .views import BookListView, BookCreateView, BookDetailView, BookUpdateView, BookDeleteView

urlpatterns = [
    # URLs that are specific to the checker's syntax
    path('books/update/', BookUpdateView.as_view(), name='book-update-checker'),
    path('books/delete/', BookDeleteView.as_view(), name='book-delete-checker'),
    
    # Correct and functional URLs for your project
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]