from django.contrib import admin
from .models import Employee, Meal, Order
# Register your models here.

admin.site.register(Employee)
admin.site.register(Meal)
admin.site.register(Order)