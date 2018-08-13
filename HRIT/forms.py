from django import forms
from HRIT.models import Employee
from HRIT.models import Computer


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'department_name', 'training_programs', 'computers')

class ComputerForm(forms.ModelForm):

    class Meta:
        model = Computer
        fields = ('make', 'manufacturer', 'purchase_date')
