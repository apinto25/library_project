from datetime import datetime

from django.db import models
from django.db.models import Q, Count
from django.contrib.postgres.search import TrigramSimilarity


class BookManager(models.Manager):
    """Managers for Book model."""

    def search_books_by_title(self, kword):
        result = self.filter(
            title__icontains=kword,
        )
        return result

    def search_books_by_title_trg(self, kword):
        if kword:
            result = self.filter(
                title__trigram_similar=kword,
            )
            return result
        else:
            return self.all()[:10]

    def search_books_by_date(self, kword, initial_date, final_date):

        initial_date = datetime.strptime(initial_date, "%Y-%m-%d").date()
        final_date = datetime.strptime(final_date, "%Y-%m-%d").date()

        result = self.filter(
            title__icontains=kword,
            date__range=(initial_date, final_date)
        )
        return result

    def search_books_by_category(self, category):
        return self.filter(
            category__name__icontains=category
        ).order_by('title')

    def add_book_author(self, book_id, author):
        book = self.get(id=book_id)
        book.authors.add(author)
        return book

    def num_book_loans(self):
        result = self.aggregate(
            num_loans=Count('book_loan')
        )
        return result


class CategoryManager(models.Manager):
    """Managers for Category model."""

    def category_by_author(self, author):
        return self.filter(
            book_category__authors__first_name=author
        ).distinct()

    def list_book_categories(self):
        result = self.annotate(
            num_books=Count('book_category')
        )
        return result
