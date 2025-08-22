from django.urls import path
from .views import RegisterView, LoginView, home, FollowUserView

urlpatterns = [
    path('', home, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    # Follow/Unfollow endpoints - using user_id parameter as expected by checker
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', FollowUserView.as_view(), name='unfollow-user'),
]