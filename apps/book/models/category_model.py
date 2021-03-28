from django.db import models

from apps.book.managers import CategoryManager


class Category(models.Model):
    name = models.CharField(max_length=50)

    objects = CategoryManager()

    def __str__(self):
        return self.name
