from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

# Create a router instance
router = DefaultRouter()
# Register the viewsets with the router
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
