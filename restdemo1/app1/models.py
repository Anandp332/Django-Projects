from django.db import models


class Employee(models.Model):
    Email = models.CharField(primary_key=True, max_length=40)
    Password = models.CharField(max_length=40)
    FullName = models.CharField(max_length=40)
    City = models.CharField(max_length=40)
    Salary = models.FloatField(default=0.0)

    def __dir__(self):
        return self.FullName

    class Meta:
        db_table = 'employee'
