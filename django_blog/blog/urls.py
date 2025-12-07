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

from django.urls import path
from . import views

urlpatterns = [
    # Post URLs
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs
    path('post/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
]
path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
from . import views

urlpatterns = [
    ...
    path('tags/<slug:tag_slug>/', views.PostsByTagListView.as_view(), name='posts-by-tag'),
]
path('search/', views.SearchResultsView.as_view(), name='search-results'),

