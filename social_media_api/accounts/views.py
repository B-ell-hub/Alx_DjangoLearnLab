from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterSerializer, LoginSerializer, UserProfileSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'message': 'User registered successfully',
            'token': user.auth_token.key
        })


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            'token': serializer.validated_data['token']
        })


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserProfileSerializer(
            request.user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    if request.user == user_to_follow:
        return Response({'error': "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
    request.user.following.add(user_to_follow)
    return Response({'success': f'You are now following {user_to_follow.username}.'})

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    if request.user == user_to_unfollow:
        return Response({'error': "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
    request.user.following.remove(user_to_unfollow)
    return Response({'success': f'You have unfollowed {user_to_unfollow.username}.'})
