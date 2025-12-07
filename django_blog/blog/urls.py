from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # registration
    path('register/', views.register, name='register'),

    # login/logout using Django's built-in views
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # profile
    path('profile/', views.profile, name='profile'),
]
# blog/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Posts CRUD
    path('posts/', views.PostListView.as_view(), name='posts-list'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Keep your auth urls too (if you have them)
    # path('register/', views.register, name='register'),
    # path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    # path('profile/', views.profile, name='profile'),
]
