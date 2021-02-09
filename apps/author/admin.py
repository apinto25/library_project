from django.contrib import admin

from apps.author.models.author_model import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "nationality",
    )
