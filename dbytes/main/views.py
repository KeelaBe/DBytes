from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

# Create your views here.
def index(response):
    ls = Employee.objects.get()
    return render(response, 'main/index.html', {'employeeFirstName': ls.employeeFirstName, 'employeeLastName': ls.employeeLastName})