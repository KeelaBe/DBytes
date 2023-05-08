from django.db import models

# Create your models here.
class Employee(models.Model):
    employeeName = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.employeeName

class Meal(models.Model):
    mealName = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    glutenFreeYN = models.CharField(max_length=1)
    veganYN = models.CharField(max_length=1)

    def __str__(self):
        return self.mealName

class Order(models.Model):
    mealName = models.ForeignKey('Meal', on_delete=models.CASCADE, db_column='mealName')
    employeeName = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='employeeName')
    customerName = models.CharField(max_length=100)
    notes = models.TextField()
    ordertime = models.DateTimeField()
    doneYN = models.CharField(max_length=1, default='N')

    # def __str__(self):
    #     return f'mealName: {self.mealName}, employeeName: {self.employeeName}, notes: {self.notes}, ordertime: {self.ordertime}, doneYN: {self.doneYN}'

class Customer(models.Model):
    customerName = models.CharField(max_length=50)

    def __str__(self):
        return f'customerName: {self.customerName}'