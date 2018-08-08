from django.db import models


class Training_Program(models.Model):
	"""
	Authors: Jessica Swift
	Purpose: Create training model
	"""
	startDate = models.DateTimeField(auto_now=False, auto_now_add=False)
	endDate = models.DateTimeField(auto_now=False, auto_now_add=False)
	maxAttendees = model.IntegerField(null=True, blank=True)
	name = models.CharField(max_length = 50)
	description = models.CharField(max_length = 100)

	def __str__(self):
		return f'{self.name}'

	class Meta:
		db_table = "training_program"
