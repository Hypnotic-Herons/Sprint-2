from HRIT.models import Training_Program
from django.views.generic import ListView

class Training_Program_List_View(ListView):
	'''
        Author: Jessica Swift
		Returns a list of all the training programs
	'''
	model = Training_Program
	context_object_name = 'trainingprograms'