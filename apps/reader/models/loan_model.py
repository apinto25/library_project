from django.db import models

from apps.book.models.book_model import Book
from apps.reader.models.reader_model import Reader


class Loan(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    returned = models.BooleanField()

    def __str__(self):
        return self.book.title
