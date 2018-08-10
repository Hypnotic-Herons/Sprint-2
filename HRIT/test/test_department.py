import unittest 
from django.test import TestCase
from django.urls import reverse
from HRIT.models import Department



class DepartmentTest(TestCase):

	"""
	Authors: Meghan Debity and Matthew Kelly
	Purpose: HR should be able to see all departments
	"""
	#One test with multiple assertions. If one assertion fails, the test fails.
	def test_list_departments(self):
		new_department = Department.objects.create(
			name = "IT"
		)

		#Issue a GET request
		response = self.client.get(reverse('HRIT:departments'))

		#Check that the 200 response is ok
		self.assertEqual(response.status_code, 200)

		#Check that the rended context contains 1 department
		self.assertEqual(len(response.context['department_list']), 1)
