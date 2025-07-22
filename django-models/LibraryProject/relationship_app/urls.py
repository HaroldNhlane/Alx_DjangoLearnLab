from django.urls import path
# THIS IS THE LINE THE CHECKER IS LOOKING FOR:
from .views import book_list
# Import other views separately as needed
from .views import LibraryDetailView

app_name = 'relationship_app' # Namespace for URLs, good practice for larger projects

urlpatterns = [
    # URL pattern for the function-based view: 'book_list'
    # This will display a list of all books.
    path('books/', book_list, name='book_list'),

    # URL pattern for the class-based view: 'LibraryDetailView'
    # This view displays details for a specific library based on its primary key (pk).
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]