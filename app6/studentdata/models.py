from django.db import models


# Create your models here.
class Student(models.Model):
    fullname = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    age = models.IntegerField()
    percent = models.FloatField(default=0.0)

    def __str__(self):
        return self.fullname + ',' + self.city + ',' + str(self.age) + ',' + str(self.percent)
