from HRIT.models import Computer
from django.views.generic import TemplateView

class Computer_List(TemplateView):
	"""
	Authors: Dillan Teagle
	Purpose: Create Computer List View
	"""
	template_name = 'HRIT/computers_list.html'

	def computer_list(self):
		computers = Computer.objects.all()
		return computers
