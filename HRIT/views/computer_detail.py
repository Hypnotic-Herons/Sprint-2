from HRIT.models import Computer
from django.views.generic import DetailView


class Computer_Detail_View(DetailView):
    model = Computer