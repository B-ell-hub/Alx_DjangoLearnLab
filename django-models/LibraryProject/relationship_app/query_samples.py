import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")  # Replace with your settings module
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1️⃣ Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# 2️⃣ List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# 3️⃣ Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

# Example usage
if __name__ == "__main__":
    print("Books by John Doe:")
    for book in get_books_by_author("John Doe"):
        print(book)

    print("\nBooks in Central Library:")
    for book in get_books_in_library("Central Library"):
        print(book)

    print("\nLibrarian for Central Library:")
    print(get_librarian_for_library("Central Library"))
