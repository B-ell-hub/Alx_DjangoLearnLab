from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),              # / → list of posts
    path('post/new/', PostCreateView.as_view(), name='post-create'), # create
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # detail
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # update
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # delete
]
