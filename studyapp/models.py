from django.db import models

class Register(models.Model):
    regid = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=20)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    stcatnm=models.CharField(max_length=20)
    city=models.CharField(max_length=10)
    pcode=models.CharField(max_length=10)
    gender=models.CharField(max_length=20)
    status=models.IntegerField()
    role=models.CharField(max_length=50)
    dt=models.CharField(max_length=200)

class Contact(models.Model):
    
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    mobile=models.CharField(max_length=10)
    message=models.CharField(max_length=200)
    dt=models.CharField(max_length=200)

	