from django.db import models


class Department(models.Model):
	"""
	Authors: Meghan Debity and Jessica Swift
	Purpose: Create department model
	"""
	name = models.CharField(max_length = 50)

	def __str__(self):
		return f'{self.name}'

	class Meta:
		db_table = "departments"

