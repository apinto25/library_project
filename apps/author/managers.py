from django.db import models
from django.db.models import Q


class AuthorManager(models.Manager):
    """Managers for Author model."""

    def search_authors(self, kword):
        result = self.filter(
            Q(first_name__icontains=kword) | Q(last_name__icontains=kword)
        )
        return result

    def search_exclude_authors(self, kword):
        result = self.filter(
            first_name__icontains=kword
        ).exclude(age=36)
        return result

    def search_compare_age_authors(self, kword):
        result = self.filter(
            age__gt=40,
            age__lt=65
        ).filter(
            first_name__icontains=kword
        ).order_by("last_name", "first_name")
        return result
