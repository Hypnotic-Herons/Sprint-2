import unittest
from django.test import TestCase
from django.urls import reverse
from HRIT.models import Employee, Department


class EmployeeTest(TestCase):

    def test_employee_list(self):
        department = Department.objects.create(
            name = "IT"
        )
        employee = Employee.objects.create(
            first_name="Dillan",
            last_name="Teagle",
            department_name= Department.objects.get(pk=1)
        )

        response = self.client.get(reverse('HRIT:employees'))

        self.assertEqual(response.status_code, 200)
