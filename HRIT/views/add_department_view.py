from django.shortcuts import render, redirect
from HRIT.models import Department
from django.views.generic import FormView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from HRIT.forms import DepartmentForm


class DepartmentFormView(FormView):
    template_name = 'HRIT/department_list.html'
    form_class = DepartmentForm

    success_url = '/HRIT/Department/'

    def form_valid(self, form):
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
        form.save()
        return redirect('/HRIT/department/')


class Department_Delete(DeleteView):
    model = Department
    success_url = reverse_lazy('/HRIT/department/')
