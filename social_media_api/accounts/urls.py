from django.urls import path
from .views import RegisterView, LoginView, home # Import the new home view

urlpatterns = [
    # This new path maps the empty string to the home view
    path('', home, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
