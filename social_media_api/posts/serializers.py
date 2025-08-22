from rest_framework import serializers
from .models import Post, Comment, Like
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model.
    """
    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Like
        fields = ['id', 'user', 'user_id', 'created_at']
        read_only_fields = ['user', 'user_id', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.
    It includes a read-only field for the author's username and like information.
    """
    author = serializers.ReadOnlyField(source='author.username')
    likes_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'likes_count', 'is_liked']
        read_only_fields = ['author', 'post']

    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            content_type = ContentType.objects.get_for_model(Comment)
            return Like.objects.filter(
                user=request.user, 
                content_type=content_type, 
                object_id=obj.id
            ).exists()
        return False

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model.
    It includes nested comments, like information, and a read-only author field.
    """
    author = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'author', 'comments', 
            'created_at', 'updated_at', 'likes_count', 'is_liked',
            'comments_count'
        ]
        read_only_fields = ['author']

    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            content_type = ContentType.objects.get_for_model(Post)
            return Like.objects.filter(
                user=request.user, 
                content_type=content_type, 
                object_id=obj.id
            ).exists()
        return False
    
    def get_comments_count(self, obj):
        return obj.comments.count()