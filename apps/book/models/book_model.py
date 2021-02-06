from django.db import models

from apps.author.models.author_model import Author
from apps.book.models.category_model import Category


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=50)
    date = models.DateField()
    cover = models.ImageField(upload_to="cover")
    visits = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    