from django.db import models

# Create your models here.
class Employee(models.Model):
    ename=models.CharField(max_length=300)
    eno=models.IntegerField()
    esal=models.IntegerField()
    eaddr=models.CharField(max_length=300)
