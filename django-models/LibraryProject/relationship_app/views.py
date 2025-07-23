from django.shortcuts import render, redirect # Make sure 'redirect' is here
from django.contrib import messages # Make sure 'messages' is here
# Import LoginView and LogoutView from Django's built-in auth views
from django.contrib.auth import views as auth_views # This import is not directly used in views.py, but shown here for context/consistency from urls.py

# CHANGE THIS LINE: Use the more specific import path for DetailView
from django.views.generic.detail import DetailView

# Separate imports for models as previously discussed
from .models import Book
from .models import Library
from .models import Author

# NEW: Import for the custom registration form
from .forms import UserRegisterForm


# Existing function-based view
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

# Existing class-based view
class LibraryDetailView(DetailView):
    """
    Class-based view to display details for a specific library.
    Utilizes Django's DetailView.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# NEW: Function-based view for user registration
def register(request):
    """
    Handles user registration.
    Displays a form for new users to sign up.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # Saves the user to the database
            username = form.cleaned_data.get('username')
            # Display a success message
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login') # Redirect to the login page (name defined in urls.py)
    else:
        form = UserRegisterForm() # Display a blank form for GET requests
    return render(request, 'relationship_app/register.html', {'form': form})