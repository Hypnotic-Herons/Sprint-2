from django.urls import path
from HRIT.views import Computer_List, EmployeeView


app_name = 'HRIT'

urlpatterns = [
    path('employees/', views.EmployeeView.as_view(), name='employees'),
    path('computers/', views.Computer_List.as_view(), name='computers'),
]