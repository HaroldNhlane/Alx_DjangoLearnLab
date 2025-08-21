from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for managing posts.
    Provides CRUD operations, filtering, and pagination.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
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
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get the list of users the current user is following
        following_users = self.request.user.following.all()
        # Return posts from those users, ordered by creation date
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
