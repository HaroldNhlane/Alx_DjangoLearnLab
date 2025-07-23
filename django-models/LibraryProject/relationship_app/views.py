from django.shortcuts import render, redirect
from django.contrib import messages
# --- START: ESSENTIAL IMPORTS (Including those for the checker) ---
from django.contrib.auth import login # This import is required
from django.contrib.auth.forms import UserCreationForm # This import is also required
from django.contrib.auth.views import LoginView, LogoutView # For consistency and use in urls.py
# --- NEW IMPORTS FOR RBAC ---
from django.contrib.auth.decorators import user_passes_test # Required for @user_passes_test
from .models import UserProfile # Required to check user roles from UserProfile
# --- END: ESSENTIAL IMPORTS ---

from django.views.generic.detail import DetailView

from .models import Book # Existing model import
from .models import Library # Existing model import
from .models import Author # Existing model import

from .forms import UserRegisterForm # Your custom registration form


# Helper functions for role-based access
# --- NEW CODE: ROLE CHECKER FUNCTIONS ---
def is_admin(user):
    """Checks if the user has the 'Admin' role in their UserProfile."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    """Checks if the user has the 'Librarian' role in their UserProfile."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    """Checks if the user has the 'Member' role in their UserProfile."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'
# --- END NEW CODE ---


# LibraryProject/relationship_app/views.py

# ... (all existing imports and helper functions) ...

# Existing function-based view to list all books
# --- CHANGE THIS FUNCTION NAME ---
def list_books(request): # Renamed from book_list to list_books
    """
    Function-based view to list all books.
    Renders a template displaying book titles and their authors.
    """
    books = Book.objects.all().order_by('title')
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

# ... (rest of your views.py file) ...

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
    Displays a form for new users to sign up.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save() # Saves the user to the database
            username = form.cleaned_data.get('username')
            # Display a success message
            messages.success(request, f'Account created for {username}! You can now log in.')
            # Optional: You can uncomment the line below to automatically log the user in after registration
            # login(request, user)
            # --- CRITICAL FIX: Redirect to the namespaced login URL ---
            return redirect('relationship_app:login')
    else:
        form = UserRegisterForm() # Display a blank form for GET requests
    return render(request, 'relationship_app/register.html', {'form': form})

# --- NEW CODE: ADMIN VIEW ---
@user_passes_test(is_admin, login_url='/relationship_app/login/') # Redirect to login if not admin
def admin_view(request):
    """View accessible only to Admin users."""
    return render(request, 'relationship_app/admin_view.html', {'message': 'Welcome, Admin!'})
# --- END NEW CODE ---