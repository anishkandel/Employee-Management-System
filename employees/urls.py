from django.urls import path
from . import views
from .views import export_employees

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_employee, name='add_employee'),
    path('delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('update/<int:id>/', views.update_employee, name='update_employee'),
    path('search/', views.search_employee, name='search_employee'),
    path('employees/export/', export_employees, name='export_employees'),
]