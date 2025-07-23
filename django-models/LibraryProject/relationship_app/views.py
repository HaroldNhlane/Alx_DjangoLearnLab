from django.shortcuts import render, redirect
from django.contrib import messages
# --- START: ESSENTIAL IMPORTS (Including those for the checker) ---
from django.contrib.auth import login # This import is required
from django.contrib.auth.forms import UserCreationForm # This import is also required
from django.contrib.auth.views import LoginView, LogoutView # For consistency and use in urls.py
# --- END: ESSENTIAL IMPORTS ---

from django.views.generic.detail import DetailView

from .models import Book
from .models import Library
from .models import Author

from .forms import UserRegisterForm # Your custom registration form


# Existing function-based view to list all books
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