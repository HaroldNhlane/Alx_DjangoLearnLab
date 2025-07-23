from django.urls import path
# --- START: ESSENTIAL IMPORTS FOR VIEWS ---
from .views import list_books, register, admin_view, librarian_view, member_view
# --- END: ESSENTIAL IMPORTS FOR VIEWS ---
from django.contrib.auth import views as auth_views

from .views import LibraryDetailView

app_name = 'relationship_app' # Namespace for URLs

# --- CRITICAL FIX: Changed 'rlpatterns' to 'urlpatterns' ---
urlpatterns = [
    # Existing URL patterns
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URL Patterns
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Role-based dashboard views
    path('admin_dashboard/', admin_view, name='admin_dashboard'),
    path('librarian_dashboard/', librarian_view, name='librarian_dashboard'),
    path('member_dashboard/', member_view, name='member_dashboard'),
]