from django.shortcuts import render, redirect
from django.contrib import messages
# --- START: ESSENTIAL IMPORTS ---
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm # <-- Required for register view
from django.contrib.auth.views import LoginView, LogoutView
# --- NEW IMPORTS FOR RBAC ---
from django.contrib.auth.decorators import user_passes_test # Required for @user_passes_test
from .models import UserProfile # Required to check user roles from UserProfile
# --- END: ESSENTIAL IMPORTS ---

from django.views.generic.detail import DetailView

from .models import Book
from .models import Library
from .models import Author

# --- REMOVED: from .forms import UserRegisterForm (since we're using UserCreationForm) ---


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
def list_books(request): # Renamed from book_list to list_books for checker compliance
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
        form = UserCreationForm(request.POST) # <-- Now uses UserCreationForm
        if form.is_valid():
            user = form.save() # Saves the user to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('relationship_app:login')
    else:
        form = UserCreationForm() # <-- Now uses UserCreationForm
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