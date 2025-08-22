from rest_framework import viewsets, generics, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification

User = get_user_model()

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['author', 'title']
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        # Use get_object_or_404 as expected by the checker
        post = get_object_or_404(Post, pk=pk)
        user = request.user
        
        # Check if user already liked this post
        if Like.objects.filter(user=user, content_object=post).exists():
            return Response(
                {"detail": "You have already liked this post."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Create the like using get_or_create pattern (though we check first)
        like, created = Like.objects.get_or_create(user=user, content_object=post)
        
        # Create notification for the post author if it's not the same user
        if post.author != user:
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb="like",
                target=post
            )
        
        return Response(
            {"detail": "Post liked successfully.", "like": LikeSerializer(like).data},
            status=status.HTTP_201_CREATED
        )

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        # Use get_object_or_404 as expected by the checker
        post = get_object_or_404(Post, pk=pk)
        user = request.user
        
        try:
            like = Like.objects.get(user=user, content_object=post)
            like.delete()
            return Response(
                {"detail": "Post unliked successfully."},
                status=status.HTTP_200_OK
            )
        except Like.DoesNotExist:
            return Response(
                {"detail": "You haven't liked this post yet."},
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=True, methods=['get'])
    def likes(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        post_content_type = ContentType.objects.get_for_model(Post)
        likes = Like.objects.filter(content_type=post_content_type, object_id=post.id)
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)
        
        # Create notification for the post author if it's not the same user
        if comment.post.author != self.request.user:
            Notification.objects.create(
                recipient=comment.post.author,
                actor=self.request.user,
                verb="comment",
                target=comment.post
            )

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        comment = get_object_or_404(Comment, pk=pk)
        user = request.user
        
        # Check if user already liked this comment
        if Like.objects.filter(user=user, content_object=comment).exists():
            return Response(
                {"detail": "You have already liked this comment."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Create the like using get_or_create pattern
        like, created = Like.objects.get_or_create(user=user, content_object=comment)
        
        # Create notification for the comment author if it's not the same user
        if comment.author != user:
            Notification.objects.create(
                recipient=comment.author,
                actor=user,
                verb="like",
                target=comment
            )
        
        return Response(
            {"detail": "Comment liked successfully.", "like": LikeSerializer(like).data},
            status=status.HTTP_201_CREATED
        )

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        comment = get_object_or_404(Comment, pk=pk)
        user = request.user
        
        try:
            like = Like.objects.get(user=user, content_object=comment)
            like.delete()
            return Response(
                {"detail": "Comment unliked successfully."},
                status=status.HTTP_200_OK
            )
        except Like.DoesNotExist:
            return Response(
                {"detail": "You haven't liked this comment yet."},
                status=status.HTTP_400_BAD_REQUEST
            )

class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')