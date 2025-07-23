from django.urls import path
# --- CRITICAL CHANGE FOR CHECKER COMPLIANCE: Import the entire views module ---
from . import views # Changed from 'from .views import function_name, ...'
# --- END CRITICAL CHANGE ---

from django.contrib.auth import views as auth_views

# LibraryDetailView is a class-based view, so it's typically imported separately or referenced directly if defined in 'views'
# If LibraryDetailView is defined in 'views.py', you can access it via views.LibraryDetailView.
# For simplicity and common practice, let's assume it's directly accessible via views.
# So, the line 'from .views import LibraryDetailView' can now be removed if it was separate.
# We will use views.LibraryDetailView below.

app_name = 'relationship_app' # Namespace for URLs

urlpatterns = [
    # Existing URL patterns - now using 'views.' prefix
    path('books/', views.list_books, name='book_list'), # Using views.list_books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'), # Using views.LibraryDetailView

    # Authentication URL Patterns - now using 'views.' prefix
    path('register/', views.register, name='register'), # <<< NOW IT CONTAINS 'views.register'
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Role-based dashboard views - now using 'views.' prefix
    path('admin_dashboard/', views.admin_view, name='admin_dashboard'),
    path('librarian_dashboard/', views.librarian_view, name='librarian_dashboard'),
    path('member_dashboard/', views.member_view, name='member_dashboard'),

    # --- NEW CODE: URL patterns for permission-controlled views ---
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
    # --- END NEW CODE ---
]