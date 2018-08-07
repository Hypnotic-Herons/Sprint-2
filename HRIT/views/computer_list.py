from HRIT.models import Computer

class Computer_List(TemplateView):
     """
	Authors: Dillan Teagle
	Purpose: Create Computer List View
	"""
    template_name = 'HRIT/computers.html'

    def customer_list(self):
        computers = Computers.objects.all()
        return computers
