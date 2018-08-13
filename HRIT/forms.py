from django import forms
from HRIT.models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'department_name', 'training_programs', 'computers')
