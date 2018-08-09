from django.urls import path
from HRIT.views import Computer_List, EmployeeView, Department_List_View


app_name = 'HRIT'

urlpatterns = [
    path('employees/', EmployeeView.as_view(), name='employees'),
    path('computers/', Computer_List.as_view(), name='computers'),
	path('departments/', Department_List_View.as_view(), name='departments'),
]