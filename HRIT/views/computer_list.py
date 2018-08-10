from HRIT.models import Computer
from django.views.generic import TemplateView, ListView


class Computer_List(ListView):
	"""Authors: Dillan Teagle
	Purpose: Create Computer List View
	"""
	model = Computer
	context_object_name = 'computer_list'
