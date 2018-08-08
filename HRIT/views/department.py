from HRIT.models import Department
from django.views.generic import TemplateView

class DepartmentView(TemplateView):
    """[summary]
    API endpoint that allows departments to be viewed and edited.
    """
    template_name = 'HRIT/departments.html'
    def department_list(self):
        departments = Department.objects.all()
        return departments
