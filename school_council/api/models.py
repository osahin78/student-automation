from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    surname=models.CharField(max_length=100,null=False,blank=False)
    stdNumber=models.CharField(max_length=20,null=False,blank=False,unique=True)
    grades=models.JSONField()

        