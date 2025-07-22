from django.shortcuts import render
from django.views.generic import DetailView # Already imported
from .models import Book, Library, Author # Already imported

def book_list(request):
    """
    Function-based view to list all books.
    Renders a template displaying book titles and their authors.
    """
    books = Book.objects.all().order_by('title')
    context = {
        'books': books
    }
    return render(request, 'list_books.html', context)

class LibraryDetailView(DetailView):
    """
    Class-based view to display details for a specific library.
    Utilizes Django's DetailView.
    """
    model = Library # Specifies the model this view will operate on
    template_name = 'library_detail.html' # The template to render
    context_object_name = 'library' # The name of the variable in the template context

    # No need to override get_context_data if you just want the object itself,
    # as DetailView automatically adds it to the context under context_object_name
    # or 'object' by default.
    # The related books are accessed directly via `library.books.all` in the template.
