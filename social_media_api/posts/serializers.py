from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'title',
            'content',
            'created_at',
            'updated_at'
        ]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'author',
            'content',
            'created_at',
            'updated_at'
        ]
from rest_framework import serializers
from .models import Post, Like

class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'likes_count']
from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    target_type = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'actor_username', 'verb', 'target_type', 'read', 'timestamp']

    def get_target_type(self, obj):
        return obj.target_ct.model if obj.target_ct else None
