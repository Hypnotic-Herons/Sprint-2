from HRIT.models import Employee
from django.views.generic import DetailView


class Employee_Detail_View(DetailView):
    model = Employee