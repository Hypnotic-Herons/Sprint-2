from HRIT.models import Training_Program
from django.views.generic import TemplateView

class TrainingProgramView(TemplateView):
	'''
        Author: Jessica Swift
		Returns a list of all the training programs
	'''
	template_name = 'HRIT/trainingprogram.html'

	def training_program_list(self):
		training_programs = Training_Program.objects.all()
		print(training_programs)
		return training_programs