from django.urls import path
from .views.admin_view import admin_view
from .views.librarian_view import librarian_view
from .views.member_view import member_view
from .views.book_views import add_book, edit_book, delete_book

urlpatterns = [
    # Role-based views
    path("admin-role/", admin_view, name="admin_view"),
    path("librarian-role/", librarian_view, name="librarian_view"),
    path("member-role/", member_view, name="member_view"),

    # Book management views
    path("books/add/", add_book, name="add_book"),
    path("books/edit/<int:pk>/", edit_book, name="edit_book"),
    path("books/delete/<int:pk>/", delete_book, name="delete_book"),
]
