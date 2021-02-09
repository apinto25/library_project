from django.db import models
from django.db.models import Q


class AuthorManager(models.Manager):
    """Managers for Author model."""

    def search_authors(self, kowrd):
        result = self.filter(
            Q(first_name__icontains=kowrd) | Q(last_name__icontains=kowrd)
        )
        return result
