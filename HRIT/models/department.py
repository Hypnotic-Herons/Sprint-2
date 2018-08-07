from django.db import models


class Department(models.Model):
	"""
	Authors: Meghan Debity and Jessica Swift
	Purpose: Create department model
	"""


	name = models.CharField(max_length = 30)
	budget = models.CharField(max_legth = 30)
	supervisorId = models.ForeignKey('Employee', on_delete=models.CASCADE)

	class Meta:
		db_table = "department"
