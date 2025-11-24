from django.contrib import admin
from django.urls import path, include

from django.urls import path
from .views import BookList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # This connects your API app URLs
]


