from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        tokens = get_tokens_for_user(user)
        data = {
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            },
            "tokens": tokens
        }
        return Response(data, status=status.HTTP_201_CREATED)

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """
        Blacklist the provided refresh token.
        Expected payload: {"refresh": "<refresh_token>"}
        """
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)
