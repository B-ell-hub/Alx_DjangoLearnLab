# bookshelf/views.py
from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import BookForm

# Safe search example
def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)  # Parameterized ORM query
    return render(request, 'bookshelf/book_list.html', {'books': books})
