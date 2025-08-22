from rest_framework import viewsets, generics, permissions  # Added permissions import
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for managing posts.
    Provides CRUD operations, filtering, and pagination.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]  # Changed to permissions.
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['author', 'title']
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        """
        Sets the author of the post to the current user.
        """
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset for managing comments.
    Provides CRUD operations with proper permissions.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]  # Changed to permissions.

    def perform_create(self, serializer):
        """
        Sets the author of the comment to the current user.
        """
        serializer.save(author=self.request.user)


class UserFeedView(generics.ListAPIView):
    """
    A view to display posts from users the current user is following.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]  # Changed to permissions.IsAuthenticated

    def get_queryset(self):
        # Get the list of users the current user is following.
        # This uses the related_name 'following'.
        following_users = self.request.user.following.all()
        # Return posts from those users, ordered by creation date
        return Post.objects.filter(author__in=following_users).order_by('-created_at')