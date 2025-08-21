from django.urls import path
from .views import RegisterView, LoginView, home, FollowUserView

urlpatterns = [
    path('', home, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    # This is the new path for the follow/unfollow functionality
    path('follow/<int:pk>/', FollowUserView.as_view(), name='follow-user'),
]
