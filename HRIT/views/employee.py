from HRIT.models import Employee

class EmployeeView(TemplateView):
	'''
		Returns a list of all the employees
	'''
	template_name = 'employeelist.html'

	def employee_list(self):
		employees = Employee.objects.all()
		print(employees)
		return employees
