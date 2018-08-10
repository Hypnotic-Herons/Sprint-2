from django.db import models


class Computer(models.Model):
	"""
	Authors: Dillan Teagle
	Purpose: Create department model
	Updates: Removing employee foreign key and adding a many to many relationship to for computers to the employee model. Added absolute url function.
	"""
	manufacturer = models.CharField(max_length=120)
	make = models.CharField(max_length=120)
	purchase_date = models.DateField()


	def get_absolute_url(self):
		return reverse('HRIT:computer_detail', kwargs={'pk': self.pk})

	def __str__(self):
		return (f'{self.manufacturer} {self.make}')

	class Meta:
		db_table = "computers"

