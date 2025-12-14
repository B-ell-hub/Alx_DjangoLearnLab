from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, feed

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', feed, name='feed'),
]
from django.urls import path
from .views import LikePostView, UnlikePostView

urlpatterns = [
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like_post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike_post'),
]
from django.urls import path
from .views import NotificationListView

urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications'),
]
