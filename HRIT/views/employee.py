from HRIT.models import Employee
from django.views.generic import TemplateView

class EmployeeView(TemplateView):
	'''
		Returns a list of all the employees
	'''
	template_name = 'HRIT/employees.html'

	def employee_list(self):
		employees = Employee.objects.all()
		return employees
