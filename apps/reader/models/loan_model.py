from django.db import models
from django.db.models.signals import post_delete

from apps.book.models.book_model import Book
from apps.reader.models.reader_model import Reader
from apps.reader.managers import LoanManager


class Loan(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='book_loan'
    )
    loan_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    returned = models.BooleanField()

    objects = LoanManager()

    def save(self, *args, **kwargs):
        self.book.stock -= 1
        self.book.save()
        super(Loan, self).save(*args, **kwargs)


    def __str__(self):
        return self.book.title

def update_book_stock(sender, instance, **kwargs):
    instance.book.stock += 1
    instance.book.save()

post_delete.connect(update_book_stock, sender=Loan)
