from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    marks = models.IntegerField()
    class Meta:
        db_table = 'Students'
    def __str__(self):
        return self.name + "," + self.email + "," + self.address + "," + str(self.marks)


# Create your models here.
