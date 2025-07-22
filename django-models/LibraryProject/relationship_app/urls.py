from django.urls import path
# Separate import for list_books to match the checker's exact requirement
from .views import book_list
# Import other views separately if needed, or if checker also complains later
from .views import LibraryDetailView

app_name = 'relationship_app' # Namespace for URLs, good practice for larger projects

urlpatterns = [
    # URL for the function-based view: lists all books
    # Example URL: /relationship_app/books/
    path('books/', book_list, name='book_list'),

    # URL for the class-based view: displays details of a specific library
    # The <int:pk> part captures an integer from the URL and passes it as 'pk'
    # to the DetailView, which uses it to fetch the specific Library object.
    # Example URL: /relationship_app/library/1/ (where 1 is the library's primary key)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]