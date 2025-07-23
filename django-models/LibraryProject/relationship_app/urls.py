from django.urls import path
from .views import book_list, register
# Import specific authentication views from Django
from django.contrib.auth import views as auth_views # This alias is important

from .views import LibraryDetailView

app_name = 'relationship_app' # Namespace for URLs

urlpatterns = [
    # Existing URL patterns
    path('books/', book_list, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # NEW: Authentication URL Patterns
    # Registration view
    path('register/', register, name='register'),

    # Login view (uses Django's built-in LoginView)
    # >>> ENSURE THIS LINE IS PRESENT EXACTLY AS SHOWN <<<
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Logout view (uses Django's built-in LogoutView)
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]