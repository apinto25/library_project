from django.contrib import admin

from apps.book.models.book_model import Book
from apps.book.models.category_model import Category


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "date",
        "visits",
    )


@admin.register(Category)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
