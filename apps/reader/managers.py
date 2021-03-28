from django.db import models
from django.db.models import Q, Count, Avg
from django.db.models.functions import Lower


class LoanManager(models.Manager):
    """Managers for loan model."""

    def book_average_age(self):
        result = self.filter(
            book__id='1'
        ).aggregate(
            average_age=Avg('reader__age')
        )
        return result

    def num_loan_books(self):
        result = self.values(
            'book'
        ).annotate(
            num_loans=Count('book'),
            title=Lower('book__title')
        )
        return result
