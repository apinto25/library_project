from django.contrib import admin
from django.urls import path

from apps.reader import views

urlpatterns = [
    path(
        'loan/add/',
        views.RegisterLoan.as_view(),
        name="add_loan"
    ),
    path(
        'loan/multiple-add/',
        views.RegisterMultipleLoan.as_view(),
        name="add_multiple_loan"
    ),
]
