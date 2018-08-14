from django.urls import path
from HRIT.views import Computer_List, EmployeeView, Department_List_View, Training_Program_List_View, Training_Program_Form_View, Employee_Detail_View, EmployeeFormView, Computer_Detail_View, ComputerFormView, DepartmentFormView

app_name = 'HRIT'

urlpatterns = [
    path('employees/', EmployeeView.as_view(), name='employees'),
    path('employees/<int:pk>/', Employee_Detail_View.as_view(), name='employee_detail'),
    path('employees/add/', EmployeeFormView.as_view(), name='employee_form'),
    path('computers/', Computer_List.as_view(), name='computers'),
	  path('computers/<int:pk>/', Computer_Detail_View.as_view(), name='computer_detail'),
	  path('computers/add/', ComputerFormView.as_view(), name='computer_form'),
	  path('departments/', Department_List_View.as_view(), name='departments'),
    path('departments/add', DepartmentFormView.as_view(), name='department_form'),
    path('trainingprograms/', Training_Program_List_View.as_view(), name='trainingprograms'),
    path('trainingprograms/<int:pk>/', Training_Program_List_View.as_view(), name='trainingprogram_detail'),
    path('trainingprograms/add/', Training_Program_Form_View.as_view(), name='new_training')
]