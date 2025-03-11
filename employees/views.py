from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm
from django.http import JsonResponse


def home(request):
    employees = Employee.objects.all()
    return render(request, 'employees/home.html', {'employees': employees})

def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request, 'employees/home.html', {'form': form})


from django.db import connection

def delete_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()

    # Reset the ID sequence after deletion
    with connection.cursor() as cursor:
        cursor.execute("UPDATE sqlite_sequence SET seq = (SELECT MAX(id) FROM employees_employee) WHERE name='employees_employee'")

    return redirect('home')


from django.db import connection

def delete_all_employees(request):
    Employee.objects.all().delete()  # Delete all employees

    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='employees_employee'")  # Reset sequence

    return redirect('home')



def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home')  # Change 'home' to your actual URL name
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/update.html', {'form': form, 'employee': employee})




from django.db.models import Q

def search_employee(request):
    query = request.GET.get('search-query', '').strip()  # Remove leading/trailing spaces

    employees = Employee.objects.filter(
        Q(id__icontains=query) |  # Case-insensitive exact match for ID
        Q(name__icontains=query) |  # Case-insensitive partial match for Name
        Q(mobile__icontains=query) |  # Case-insensitive partial match for Mobile
        Q(email__icontains=query) |  # Case-insensitive partial match for Email
        Q(address__icontains=query) |  # Case-insensitive partial match for Address
        Q(gender__iexact=query) |  # Case-insensitive exact match for Gender
        Q(dob__icontains=query)  # Case-insensitive partial match for Date of Birth
    )

    return render(request, 'employees/home.html', {'employees': employees})





#CSV Export
import csv
from django.http import HttpResponse
from .models import Employee  # Import your Employee model

def export_employees(request):
    # Set response headers for CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employees.csv"'

    writer = csv.writer(response)
    
    # Write the header row
    writer.writerow(['ID', 'Name', 'Mobile', 'Email', 'Address', 'Gender', 'DOB'])

    # Write employee data rows
    employees = Employee.objects.all()
    for emp in employees:
        writer.writerow([emp.id, emp.name, emp.mobile, emp.email, emp.address, emp.gender, emp.dob])

    return response
