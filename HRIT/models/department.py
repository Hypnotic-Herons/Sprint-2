from django.db import models


class Department(models.Model):
	name = models.CharField(max_length = 30)
	budget = models.CharField(max_legth = 30)
	supervisorId = models.ForeignKey('Employee', on_delete=models.CASCADE)

	class Meta:
		db_table = "department"
