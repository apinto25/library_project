from django.db import models

from apps.author.models.author_model import Author
from apps.book.models.category_model import Category
from apps.book.managers import BookManager


class Book(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="book_category"
    )
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=50)
    date = models.DateField()
    cover = models.ImageField(upload_to="cover")
    visits = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)

    objects = BookManager()

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['title', 'date']

    def __str__(self):
        return self.title
