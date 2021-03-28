from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.book.models.book_model import Book


class ListBooks(ListView):
    context_object_name = "books_list"
    template_name = "book/list.html"

    def get_queryset(self):
        kword = self.request.GET.get("kword", "")
        initial_date = self.request.GET.get("initial_date", "")
        final_date = self.request.GET.get("final_date", "")

        if initial_date and final_date:
            return Book.objects.search_books_by_date(kword, initial_date, final_date)
        else:
            return Book.objects.search_books_by_title(kword)


class ListBooksCategory(ListView):
    context_object_name = "books_list_category"
    template_name = "book/list_category.html"

    def get_queryset(self):
        category = self.request.GET.get("category", "")
        return Book.objects.search_books_by_category(category)



class BookDetailView(DetailView):
    model = Book
    template_name = "book/detail.html"
