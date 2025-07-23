from django.urls import path
# --- START: ESSENTIAL IMPORT FOR VIEWS ---
from .views import book_list, register # <<< ENSURE THIS LINE IS PRESENT AND CORRECT
# --- END: ESSENTIAL IMPORT FOR VIEWS ---
from django.contrib.auth import views as auth_views

from .views import LibraryDetailView

app_name = 'relationship_app' # Namespace for URLs

urlpatterns = [
    # Existing URL patterns
    path('books/', book_list, name='book_list'),
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