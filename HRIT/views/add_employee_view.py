from django.shortcuts import render, redirect
from HRIT.models import Employee
from django.views.generic import FormView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from HRIT.forms import EmployeeForm


class EmployeeFormView(FormView):
    template_name = 'HRIT/employee_form.html'
    form_class = EmployeeForm

    success_url = '/HRIT/employees/'

    def form_valid(self, form):
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
        form.save()
        return redirect('/HRIT/employees/')


class Employee_Delete(DeleteView):
    model = Employee
    success_url = reverse_lazy('/HRIT/employees/')
