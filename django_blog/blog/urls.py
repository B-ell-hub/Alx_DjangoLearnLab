from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    # Existing post URLs
    path('', PostListView.as_view(), name='post-list'),              # / → list of posts
    path('post/new/', PostCreateView.as_view(), name='post-create'), # create
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # detail
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # update
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # delete
]
# Comment URLs
path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
from django.urls import path
from . import views

path('post/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),

