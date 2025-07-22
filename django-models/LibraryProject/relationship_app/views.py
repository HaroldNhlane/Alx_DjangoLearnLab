from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library, Author # Ensure all necessary models are imported

def book_list(request):
    """
    Function-based view to list all books.
    Renders a template displaying book titles and their authors.
    """
    books = Book.objects.all().order_by('title')
    context = {
        'books': books
    }
    # CHANGE THIS LINE: Use the explicit app-prefixed template path
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    """
    Class-based view to display details for a specific library.
    Utilizes Django's DetailView.
    """
    model = Library
    # Also ensure consistency here, though checker didn't complain about this yet
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'