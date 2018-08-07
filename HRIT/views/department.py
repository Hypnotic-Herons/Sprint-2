from django.db import models

class DepartmentView(TemplateView):
    """[summary]
    API endpoint that allows departments to be viewed and edited.
    """
    template_name = 'departmentlist.html'
    def department_list(self):
        departments = Department.objects.all()
        return departments
