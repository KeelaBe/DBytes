from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Meal, Order
from .forms import PlaceOrder
from datetime import datetime
from django.db.models import Max, Sum

# Create your views here.
def index(response):
    employees = Employee.objects.all
    meals = Meal.objects.all
    order = Order.objects.filter(ordertime__year=datetime.now().year, ordertime__month=datetime.now().month, ordertime__day=datetime.now().day).count()
    meals_today = Order.objects.filter(ordertime__year=datetime.now().year, ordertime__month=datetime.now().month, ordertime__day=datetime.now().day)
    emps = Employee.objects.all()
    mealss = Meal.objects.all()
    
    emp_orders = []
    for emp in emps:
        order_count = Order.objects.filter(ordertime__year=datetime.now().year, ordertime__month=datetime.now().month, ordertime__day=datetime.now().day, employeeName=emp).count()
        if order_count is None : 
            order_count = 0
        emp_orders.append([[emp.employeeName, order_count]])

    meal_orders = []
    for meal in mealss:
        order_count = Order.objects.filter(ordertime__year=datetime.now().year, ordertime__month=datetime.now().month, ordertime__day=datetime.now().day, mealName=meal).count()
        if order_count is None : 
            order_count = 0
        meal_orders.append([[meal.mealName, order_count]])

    daily_revenue_sum = 0
    for meal in meals_today:
        meal_name = meal.mealName
        price = Meal.objects.get(mealName=meal_name).price
        daily_revenue_sum += price

    # order_quantity = Order.objects.filter(ordertime__year=datetime.now().year(), 
    #                   ordertime__month=datetime.now().month(),
    #                   ordertime__day=datetime.now().day()).count()

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

    return render(response, 'main/index.html', {'employees': employees,
                                                 'meals': meals,
                                                'order_quantity': order,
                                                'daily_revenue': daily_revenue_sum,
                                                'employee_orders': emp_orders,
                                                'meal_orders': meal_orders})

def kitchen(response):
    orders = Order.objects.filter(doneYN='N').order_by('ordertime')

    if response.method == 'POST':
        print(response.POST)
        p = response.POST
        oid = p['OrderID']
        Order.objects.filter(id=oid).update(doneYN='Y')


    return render(response, 'main/kitchen.html', {'orders': orders})
