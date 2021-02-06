from django.db import models


class Reader(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.first_name + "-" + self.last_name
