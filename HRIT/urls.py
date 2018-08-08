from django.urls import path
from HRIT.views import Computer_List, EmployeeView, DepartmentView


app_name = 'HRIT'

urlpatterns = [
    path('employees/', EmployeeView.as_view(), name='employees'),
    path('computers/', Computer_List.as_view(), name='computers'),
	path('departments/', DepartmentView.as_view(), name='departments'),
]