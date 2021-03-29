from django.contrib import admin
from django.urls import path

from apps.book import views

urlpatterns = [
    path(
        'books/',
        views.ListBooks.as_view(),
        name="books"
    ),
    path(
        'books-trg/',
        views.ListBooksTrg.as_view(),
        name="books-trg"
    ),
    path(
        'books-category/',
        views.ListBooksCategory.as_view(),
        name="books"
    ),
    path(
        'book-detail/<pk>/',
        views.BookDetailView.as_view(),
        name="book-detail"
    ),
]
