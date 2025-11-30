from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone

# Serializer for the Book model.
# Includes custom validation to prevent future years.
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation: publication year cannot be in the future
    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer includes a nested BookSerializer to show all books of the author.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # related_name='books'

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
