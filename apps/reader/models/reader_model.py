from django.db import models

from apps.home.models.person_model import Person


class Reader(Person):

    def __str__(self):
        return self.first_name + "-" + self.last_name
