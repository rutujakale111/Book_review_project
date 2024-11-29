from django.urls import path
from . import views
from .views import BookListAPI

urlpatterns = [

    path('api/books/', BookListAPI.as_view(), name='book_list_api'),
    path('books/', BookListAPI, name='book-list'),                               # List and create books
    # path('books/<int:pk>/', book_detail, name='book-detail'),                 # Retrieve, update, and delete specific book
    # path('books/<int:book_pk>/reviews/', review_list, name='review-list'),   # List and create reviews for a specific book
    # path('books/<int:book_pk>/reviews/<int:pk>/', review_detail, name='review-detail'), 



    path('', views.BookListView.as_view(), name='book_list'),  # URL for listing all books
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),  # URL for book details
    path('new/', views.BookCreateView.as_view(), name='book_create'),  # URL for creating a book
    path('<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_update'),  # URL for editing a book
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),  # URL for deleting a book
]