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
