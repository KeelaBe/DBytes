from django.db import models

# Create your models here.
class Employee(models.Model):
    employeeID = models.IntegerField()
    employeeFirstName = models.CharField(max_length=50)
    employeeLastName = models.CharField(max_length=50)