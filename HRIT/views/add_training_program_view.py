from django.shortcuts import render, redirect
from HRIT.models import Training_Program
from django.views.generic import FormView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from HRIT.forms import Training_Program_Form


class Training_Program_Form_View(FormView):
    template_name = 'HRIT/training_program_form.html'
    form_class = Training_Program_Form

    success_url = '/HRIT/trainingprograms/'

    def form_valid(self, form):
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
        form.save()
        return redirect('/HRIT/trainingprograms/')


class Training_Program_Delete(DeleteView):
    model = Training_Program
    success_url = reverse_lazy('/HRIT/trainingprograms/')
