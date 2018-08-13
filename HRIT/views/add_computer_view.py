from django.shortcuts import render, redirect
from HRIT.models import Computer
from django.views.generic import FormView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from HRIT.forms import ComputerForm


class ComputerFormView(FormView):
    template_name = 'HRIT/computer_form.html'
    form_class = ComputerForm

    success_url = '/HRIT/computers/'

    def form_valid(self, form):
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
        form.save()
        return redirect('/HRIT/computers/')


# class Computer_Delete(DeleteView):
#     model = Computer
#     success_url = reverse_lazy('/HRIT/computers/')