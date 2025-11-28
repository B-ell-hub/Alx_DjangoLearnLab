# api/serializers.py
from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """Serializer for Book model with validation for future publication_year."""
    
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for Author model including nested books."""
    books = BookSerializer(many=True, read_only=True)  # nested serializer
    
    class Meta:
        model = Author
        fields = ['name', 'books']
