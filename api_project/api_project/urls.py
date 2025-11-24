from django.contrib import admin
from django.urls import path, include  # include is required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Connects your api app
]
