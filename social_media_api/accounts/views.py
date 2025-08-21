from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.http import HttpResponse
# Import your serializers from the accounts app
from .serializers import UserSerializer, LoginSerializer

User = get_user_model()

# This view handles requests to the root URL
def home(request):
    """
    A simple view that returns an HTTP response for the home page.
    This helps resolve the 404 error for the root URL '/'.
    """
    return HttpResponse("<h1>Welcome to the Social Media API!</h1>")

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        }, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        })

class FollowUserView(APIView):
    """
    Allows an authenticated user to follow or unfollow another user.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            target_user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        current_user = request.user

        if current_user == target_user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Corrected logic
        if current_user.following.filter(pk=target_user.pk).exists():
            current_user.following.remove(target_user)
            return Response({"detail": f"You have unfollowed {target_user.username}."}, status=status.HTTP_200_OK)
        else:
            current_user.following.add(target_user)
            return Response({"detail": f"You are now following {target_user.username}."}, status=status.HTTP_200_OK)