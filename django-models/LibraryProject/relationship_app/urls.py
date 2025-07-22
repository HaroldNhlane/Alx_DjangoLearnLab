from django.urls import path
# CHANGE THIS LINE: Explicitly import book_list and LibraryDetailView
from .views import book_list, LibraryDetailView

app_name = 'relationship_app' # Namespace for URLs, good practice for larger projects

urlpatterns = [
    # URL for the function-based view: lists all books
    # Example URL: /relationship_app/books/
    path('books/', book_list, name='book_list'), # No longer views.book_list

    # URL for the class-based view: displays details of a specific library
    # The <int:pk> part captures an integer from the URL and passes it as 'pk'
    # to the DetailView, which uses it to fetch the specific Library object.
    # Example URL: /relationship_app/library/1/ (where 1 is the library's primary key)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), # No longer views.LibraryDetailView.as_view()
]