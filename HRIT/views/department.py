from HRIT.models import Department
from django.views.generic import ListView

class Department_List_View(ListView):
    """[summary]
    API endpoint that allows departments to be viewed and edited.
    """
    model = Department
    context_object_name = 'department_list'