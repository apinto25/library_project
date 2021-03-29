from django.db import models


class Person(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    class Meta:
        # verbose_name = 'Person'
        # verbose_name_plural = 'People'
        # db_table = 'person'
        # unique_together = ['country', 'appellative']
        # constraints = [
        #     models.CheckConstraint(
        #         check=models.Q(age__gte=18), name='age_greater_18'
        #     )
        # ]
        abstract = True

    def __str__(self):
        return self.full_name
