from rest_framework import serializers
from .models import Notification
from django.contrib.auth import get_user_model

User = get_user_model()

class NotificationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Notification model.
    """
    actor = serializers.StringRelatedField()
    recipient = serializers.StringRelatedField()
    
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target', 'timestamp', 'is_read']
        read_only_fields = ['recipient', 'actor', 'verb', 'target', 'timestamp']

class NotificationUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating Notification model (mainly is_read field).
    """
    class Meta:
        model = Notification
        fields = ['is_read']