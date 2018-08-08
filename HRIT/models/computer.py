from django.db import models


class Computer(models.Model):
	"""
	Authors: Dillan Teagle
	Purpose: Create department model
	"""
	manufacturer = models.CharField(max_length=120)
	make = models.CharField(max_length=120)
	purchase_date = models.DateField()
	employee = models.ForeignKey('Employee', on_delete=models.CASCADE)

	def __str__(self):
		return (f'{self.manufacturer} {self.make}')

	class Meta:
		db_table = "computers"

