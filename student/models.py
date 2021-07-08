from django.db import models
from django.db.models.fields import PositiveSmallIntegerField

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=12)
    age=models.IntegerField(PositiveSmallIntegerField(max_length=3))
    dateofbirth=models.DateField(max_length=10)
