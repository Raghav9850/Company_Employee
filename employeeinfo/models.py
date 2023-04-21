from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Emp(models.Model):
    employeeid=models.IntegerField()
    employeename=models.CharField(max_length=50)
    Employeeaddress=models.TextField()
    mobilenumber=models.CharField(max_length=11)
    emailid=models.EmailField(max_length=50)
    aadharno=models.IntegerField()
    department=models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)