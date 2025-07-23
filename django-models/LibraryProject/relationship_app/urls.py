# LibraryProject/relationship_app/urls.py

from django.urls import path
# --- CHANGE THIS IMPORT ---
from .views import list_books, register, admin_view, librarian_view, member_view # Changed book_list to list_books
from django.contrib.auth import views as auth_views
from .views import LibraryDetailView

app_name = 'relationship_app' # Namespace for URLs

rlpatterns = [
    # Existing URL patterns
    # --- CHANGE THIS PATH REFERENCE ---
    path('books/', list_books, name='book_list'), # View is now list_books, but name can remain 'book_list'
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # NEW: Authentication URL Patterns
    # Registration view
    # <<< ENSURE 'register' IS USED HERE >>>
    path('register/', register, name='register'),

    # Login view (uses Django's built-in LoginView)
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Logout view (uses Django's built-in LogoutView)
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]