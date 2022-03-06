from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50) 

    def __str__(self):
        return self.title

class Salary(models.Model):
    pay = models.CharField(max_length=6) 

    def __str__(self):
        return self.pay
        

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    Mpesa_No= models.CharField(max_length=15)
    emp_code = models.CharField(max_length=10)
    Email= models.CharField(max_length=100)
    position= models.ForeignKey(Position,on_delete=models.CASCADE)
    Salary= models.ForeignKey(Salary,on_delete=models.CASCADE)


    
