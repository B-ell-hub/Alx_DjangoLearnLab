from django.urls import path, include
from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # This connects your API app
]

