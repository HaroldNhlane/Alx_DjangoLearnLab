from django.urls import path
from . import views # Import the views module from the current app

app_name = 'relationship_app' # Namespace for URLs, good practice for larger projects

urlpatterns = [
    # URL for the function-based view: lists all books
    # Example URL: /relationship_app/books/
    path('books/', views.book_list, name='book_list'),

    # URL for the class-based view: displays details of a specific library
    # The <int:pk> part captures an integer from the URL and passes it as 'pk'
    # to the DetailView, which uses it to fetch the specific Library object.
    # Example URL: /relationship_app/library/1/ (where 1 is the library's primary key)
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]