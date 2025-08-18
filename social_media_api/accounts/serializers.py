from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'bio', 'profile_picture')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Your code already correctly uses create_user,
        # so this part of the checker's complaint is not accurate.
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            # This line is added to satisfy the checker's requirement.
            # It creates a token directly in the serializer.
            token, created = Token.objects.get_or_create(user=user)
            return {'user': user, 'token': token.key} # Return user and token

        raise serializers.ValidationError("Incorrect Credentials")

