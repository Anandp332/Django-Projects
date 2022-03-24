from django.db import models
from django.db.models import SET_DEFAULT


class Employee(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    salary = models.IntegerField()
    class Meta:
        verbose_name_plural = 'employee'
        db_table = 'employee'
    def __str__(self):
        return self.name

class Dept(models.Model):
    name1 = models.CharField(max_length=200)
    empid = models.ForeignKey(Employee , default=1 , on_delete= models.SET_DEFAULT)
    exp = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = 'Dept'
        db_table = 'dept'
    def __str__(self):
        return self.name1




# Create your models here.
