from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer

# API ViewSet for Book
class BookViewSet(viewsets.ViewSet):
    def booklist(self, request):
        """List all books."""
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def bookcreate(self, request):
        """Create a new book."""
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def bookretrieve(self, request, pk=None):
        """Retrieve a book by ID."""
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def bookupdate(self, request, pk=None):
        """Update a book's details."""
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def bookdestroy(self, request, pk=None):
        """Delete a book."""
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# API ViewSet for Review
class ReviewViewSet(viewsets.ViewSet):
    def reviewlist(self, request, book_pk=None):
        """List all reviews for a specific book."""
        book = get_object_or_404(Book, pk=book_pk)
        reviews = book.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def reviewcreate(self, request, book_pk=None):
        """Create a new review for a specific book."""
        book = get_object_or_404(Book, pk=book_pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(book=book)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def reviewretrieve(self, request, book_pk=None, pk=None):
        """Retrieve a review by ID for a specific book."""
        book = get_object_or_404(Book, pk=book_pk)
        review = get_object_or_404(Review, pk=pk, book=book)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def reviewupdate(self, request, book_pk=None, pk=None):
        """Update a review for a specific book."""
        book = get_object_or_404(Book, pk=book_pk)
        review = get_object_or_404(Review, pk=pk, book=book)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def reviewdestroy(self, request, book_pk=None, pk=None):
        """Delete a review for a specific book."""
        book = get_object_or_404(Book, pk=book_pk)
        review = get_object_or_404(Review, pk=pk, book=book)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)