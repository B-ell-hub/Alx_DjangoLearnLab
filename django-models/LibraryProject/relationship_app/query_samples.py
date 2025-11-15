import django
import os

# Setup Django environment to allow running this as a standalone script
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models_project.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


# 1. Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books


# 2. List all books in a specific library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()
def query_librarian_for_library(library_name):

    """Retrieve the librarian for a library using Librarian.objects.get(library=...)"""

    try:

        library = Library.objects.get(name=library_name)

        librarian = Librarian.objects.get(library=library)

        print(f"The librarian for {library.name} is {librarian.name}.")

    except Library.DoesNotExist:

        print("Library not found.")

    except Librarian.DoesNotExist:

        print("No librarian assigned to this library.")



# Example usage (you can remove these before submitting if needed):
if __name__ == "__main__":
    print("Books by author John Doe:")
    print(get_books_by_author("John Doe"))

    print("\nBooks in Central Library:")
    print(get_books_in_library("Central Library"))

    print("\nLibrarian for Central Library:")
    print(query_librarian_for_library("Central Library"))
