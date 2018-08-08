from django.db import models


class Department(models.Model):
	"""
	Authors: Meghan Debity and Jessica Swift
	Purpose: Create department model
	"""
	name = models.CharField(max_length = 50)
	employeeId = models.ForeignKey('Employee', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.name}'

	class Meta:
		db_table = "departments"

