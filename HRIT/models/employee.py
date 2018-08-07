from django.db import models

class Employee(models.Model):
	'''  Model for Employee, has a foreign key of Department
		 Author: Matthew Kelly and Deanna Vickers
	'''
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	department_name = models.ForeignKey('Department', on_delete=models.CASCADE)

	class Meta:
		db_table: 'employees'

		def __str__(self):
			return (f'{self.first_name} {self.last_name})