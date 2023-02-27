from django.db import models
from django.db import IntegrityError
# Create your models here.

class Class(models.Model):
	catid = models.AutoField(primary_key=True)
	catnm=models.CharField(max_length=50,unique=True)
	caticonnm=models.CharField(max_length=500)

class Subject(models.Model):
    subcatid = models.AutoField(primary_key=True)
    catnm=models.CharField(max_length=50)
    subcatnm=models.CharField(max_length=50,unique=True)
    subcaticonnm=models.CharField(max_length=500) 

class State(models.Model):
	stcatid = models.AutoField(primary_key=True)
	stcatnm=models.CharField(max_length=50,unique=True)

class City(models.Model):
    stsubcatid = models.AutoField(primary_key=True)
    stcatnm=models.CharField(max_length=50)
    city=models.CharField(max_length=50,unique=True)
    
	
