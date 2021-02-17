from datetime import datetime

from django.db import models
from django.db.models import Q


class BookManager(models.Manager):
    """Managers for Book model."""

    def search_books_by_title(self, kword):
        result = self.filter(
            title__icontains=kword,
        )
        return result

    def search_books_by_date(self, kword, initial_date, final_date):

        initial_date = datetime.strptime(initial_date, "%Y-%m-%d").date()
        final_date = datetime.strptime(final_date, "%Y-%m-%d").date()

        result = self.filter(
            title__icontains=kword,
            date__range=(initial_date, final_date)
        )
        return result
