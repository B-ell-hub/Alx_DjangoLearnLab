# bookshelf/views.py
from django.shortcuts import render, redirect
from .forms import ExampleForm, BookForm   # <-- Add ExampleForm here
from .models import Book


# Safe search example
def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)  # Parameterized ORM query
    return render(request, 'bookshelf/book_list.html', {'books': books})
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # just print cleaned data for demonstration
            print(form.cleaned_data)
            return redirect('example_form')  # redirect to the same page after submission
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

