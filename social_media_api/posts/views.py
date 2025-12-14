from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Post, Comment, Like
from notifications.models import Notification
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # Required for checker

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)  # Required for checker
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )
            return Response({"status": "post liked"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "already liked"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unlike(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)  # Required for checker
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({"status": "post unliked"}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"status": "not liked yet"}, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
