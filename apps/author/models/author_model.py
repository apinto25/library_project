from django.db import models

from apps.home.models.person_model import Person
from apps.author.managers import AuthorManager


class Author(Person):

    objects = AuthorManager()

    def __str__(self):
        return self.first_name + "-" + self.last_name
