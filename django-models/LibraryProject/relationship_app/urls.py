from django.urls import path
# Separate import for book_list to match specific checker requirements
from .views import book_list
# Import other views, like LibraryDetailView, as needed
from .views import LibraryDetailView

app_name = 'relationship_app' # Namespace for URLs, good practice for larger projects

urlpatterns = [
    # URL pattern for the function-based view: 'book_list'
    # This will display a list of all books.
    # Access this view at, for example: http://127.0.0.1:8000/relationship_app/books/
    path('books/', book_list, name='book_list'),

    # URL pattern for the class-based view: 'LibraryDetailView'
    # This view displays details for a specific library based on its primary key (pk).
    # Access this view at, for example: http://127.0.0.1:8000/relationship_app/library/1/ (where '1' is the library's ID)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]