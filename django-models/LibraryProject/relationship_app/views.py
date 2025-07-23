# LibraryProject/relationship_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test, permission_required
# --- ADD THIS LINE ---
from django.views.generic.detail import DetailView # <-- ADD THIS IMPORT

from .models import UserProfile, Book
from .models import Library
from .models import Author

# Helper functions for role-based access
def is_admin(user):
    """Checks if the user has the 'Admin' role in their UserProfile."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    """Checks if the user has the 'Librarian' role in their UserProfile."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    """Checks if the user has the 'Member' role in their UserProfile."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# Function-based view to list all books (renamed to list_books)
def list_books(request):
    """
    Function-based view to list all books.
    Renders a template displaying book titles and their authors.
    """
    books = Book.objects.all().order_by('title')
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

# Existing class-based view for Library details
class LibraryDetailView(DetailView):
    """
    Class-based view to display details for a specific library.
    Utilizes Django's DetailView.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Function-based view for user registration
def register(request):
    """
    Handles user registration.
    Displays a form for new users to sign up using UserCreationForm.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('relationship_app:login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Role-based dashboard views
@user_passes_test(is_admin, login_url='/relationship_app/login/')
def admin_view(request):
    """View accessible only to Admin users."""
    return render(request, 'relationship_app/admin_view.html', {'message': 'Welcome, Admin!'})

@user_passes_test(is_librarian, login_url='/relationship_app/login/')
def librarian_view(request):
    """View accessible only to Librarian users."""
    return render(request, 'relationship_app/librarian_view.html', {'message': 'Welcome, Librarian!'})

@user_passes_test(is_member, login_url='/relationship_app/login/')
def member_view(request):
    """View accessible only to Member users."""
    return render(request, 'relationship_app/member_view.html', {'message': 'Welcome, Member!'})


# --- NEW CODE: Views with permission_required decorator ---
@permission_required('relationship_app.can_add_book', login_url='/relationship_app/login/')
def add_book(request):
    # This is a placeholder. You'll integrate a form here later.
    if request.method == 'POST':
        messages.success(request, "Book added successfully (placeholder)!")
        return redirect('relationship_app:book_list')
    return render(request, 'relationship_app/add_book.html', {'message': 'You have permission to add a book.'})

@permission_required('relationship_app.can_change_book', login_url='/relationship_app/login/')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # This is a placeholder. You'll integrate a form here later.
    if request.method == 'POST':
        messages.success(request, f"Book '{book.title}' edited successfully (placeholder)!")
        return redirect('relationship_app:book_list')
    return render(request, 'relationship_app/edit_book.html', {'book': book, 'message': f'You have permission to edit {book.title}.'})

@permission_required('relationship_app.can_delete_book', login_url='/relationship_app/login/')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, f"Book '{book.title}' deleted successfully!")
        return redirect('relationship_app:book_list')
    return render(request, 'relationship_app/delete_book_confirm.html', {'book': book, 'message': f'Are you sure you want to delete {book.title}?'})