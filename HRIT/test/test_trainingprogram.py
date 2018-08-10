import unittest
from django.test import TestCase
from django.urls import reverse
from datetime import datetime
from HRIT.models import Training_Program
from django.utils import timezone
import pytz
timezone.now()



class  TrainingProgramTest(TestCase):
	"""
		Authors: Meghan Debity and Matthew Kelly
		Purpose: HR should be able to see all training programs
	"""
	def	test_trainingprogram(self):
		new_trainingprogram	= Training_Program.objects.create(
			name = "Running",
			startDate =  datetime(2018, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC),
			endDate =  datetime(2018, 11, 20, 20, 8, 7, 227325, tzinfo=pytz.UTC),
			maxAttendees = 30,
			description = "learn to run"
		)

		# Issue a GET request
		response = self.client.get(reverse('HRIT:trainingprograms'))

		# Check 200 response is ok
		self.assertEqual(response.status_code, 200)

		# Check rendered content contains only one training program
		self.assertEqual(len(response.context['trainingprograms']), 1)