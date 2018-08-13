from django import forms
from HRIT.models import Employee

from HRIT.models import Training_Program


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'department_name', 'training_programs', 'computers')









class Training_Program_Form(forms.ModelForm):
    """
    Training Program Form
    Author: Meghan Debity
    Purpose: Create form on HRIT app
    """
    class Meta:
        model = Training_Program
        fields = ('startDate', 'endDate', 'maxAttendees', 'description')