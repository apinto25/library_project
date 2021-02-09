from django.contrib import admin

from apps.reader.models.loan_model import Loan
from apps.reader.models.reader_model import Reader


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "nationality",
    )


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = (
        "reader",
        "book",
        "loan_date",
        "return_date",
        "returned",
    )
