from django import forms
from HRIT.models import Employee
from HRIT.models import Computer
from HRIT.models import Department


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'department_name', 'training_programs', 'computers')
        
class DepartmentForm(forms.ModelForm):
    """
	Authors: Jessica Swift
	Purpose: Create department form
	"""
    class Meta:
        model = Department
        fields = ('name',)

class ComputerForm(forms.ModelForm):

    class Meta:
        model = Computer
        fields = ('make', 'manufacturer', 'purchase_date')

