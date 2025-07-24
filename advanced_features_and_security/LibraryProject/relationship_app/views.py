# LibraryProject/relationship_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.views.generic.detail import DetailView

from .models import UserProfile, Book, Library, Author # Consolidated model imports
from .forms import BookForm # Make sure BookForm is defined in forms.py!


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


# Function-based view to list all books
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

# Class-based view for Library details
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
        form = UserCreationForm(request.POST) # Using Django's built-in UserCreationForm
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


# --- UPDATED: Views with permission_required decorator and form handling ---
@permission_required('relationship_app.can_add_book', raise_exception=True, login_url='/relationship_app/login/')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully!")
            return redirect('relationship_app:book_list') # Corrected redirect
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True, login_url='/relationship_app/login/')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, f"Book '{book.title}' edited successfully!")
            return redirect('relationship_app:book_detail', pk=book.pk) # Corrected redirect
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True, login_url='/relationship_app/login/')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, f"Book '{book.title}' deleted successfully!")
        return redirect('relationship_app:book_list') # Corrected redirect
    return render(request, 'relationship_app/delete_book_confirm.html', {'book': book}) # Corrected template name

# --- ADDED: Book Detail View ---
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'relationship_app/book_detail.html', {'book': book})

# Additional views for other models can be added here