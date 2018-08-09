from django.db import models


class Computer(models.Model):
	"""
	Authors: Dillan Teagle
	Purpose: Create department model
	Updates: removing employee foreign key and adding a many to many relationship to for computers to the employee model
	"""
	manufacturer = models.CharField(max_length=120)
	make = models.CharField(max_length=120)
	purchase_date = models.DateField()

	def __str__(self):
		return (f'{self.manufacturer} {self.make}')

	class Meta:
		db_table = "computers"

