from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Meal, Order
from .forms import PlaceOrder
from datetime import datetime

# Create your views here.
def index(response):
    employees = Employee.objects.all
    meals = Meal.objects.all
    
    if response.method == 'POST':
        print(response.POST)
        p = response.POST
        m = Meal.objects.get(mealName=p['meal'])
        en = Employee.objects.get(employeeName=p['server-name'])
        cn = p['cust-name']
        n = p['notes']
        t = datetime.now()
        o = Order(mealName=m, employeeName=en, customerName=cn, notes=n, ordertime=t)
        o.save()

    return render(response, 'main/index.html', {'employees': employees, 'meals': meals})

def kitchen(response):
    orders = Order.objects.filter(doneYN='N').order_by('ordertime')

    if response.method == 'POST':
        print(response.POST)
        p = response.POST
        oid = p['OrderID']
        Order.objects.filter(id=oid).update(doneYN='Y')


    return render(response, 'main/kitchen.html', {'orders': orders})
