from django.shortcuts import render
from django.views.generic import ListView

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
