from datetime import date

from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from apps.reader.models.loan_model import Loan
from apps.reader.forms import LoanForm, MultipleLoanForm


class RegisterLoan(FormView):
    template_name = 'reader/add_loan.html'
    form_class = LoanForm
    success_url = '.'

    def form_valid(self, form):
        # Loan.objects.create(
        #     reader=form.cleaned_data['reader'],
        #     book=form.cleaned_data['book'],
        #     loan_date=date.today(),
        #     returned=False
        # )

        # loan = Loan(
        #     reader=form.cleaned_data['reader'],
        #     book=form.cleaned_data['book'],
        #     loan_date=date.today(),
        #     returned=False
        # )
        # loan.save()

        obj, created = Loan.objects.get_or_create(
            reader=form.cleaned_data['reader'],
            book=form.cleaned_data['book'],
            returned=False,
            defaults={
                'loan_date': date.today(),
                'returned': False
            }
        )

        if created:
            return super(RegisterLoan, self).form_valid(form)
        else:
            return HttpResponseRedirect('/')


class RegisterMultipleLoan(FormView):
    template_name = 'reader/add_multiple_loan.html'
    form_class = MultipleLoanForm
    success_url = '.'

    def form_valid(self, form):

        loan_list = []
        for book in form.cleaned_data['books']:
            loan = Loan(
                reader=form.cleaned_data['reader'],
                book=book,
                loan_date=date.today(),
                returned=False
            )
            loan_list.append(loan)

        Loan.objects.bulk_create(
            loan_list
        )        

        return super(RegisterMultipleLoan, self).form_valid(form)
