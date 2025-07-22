from django.shortcuts import render
# CHANGE THIS LINE: Use the more specific import path for DetailView
from django.views.generic.detail import DetailView

# Separate imports for models as previously discussed
from .models import Book
from .models import Library
from .models import Author

def book_list(request):
    """
    Function-based view to list all books.
    Renders a template displaying book titles and their authors.
    """
    books = Book.objects.all().order_by('title')
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    """
    Class-based view to display details for a specific library.
    Utilizes Django's DetailView.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'