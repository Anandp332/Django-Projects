from django.db import models


# Create your models here.
# Example of Many to Many relation
class Student(models.Model):
    name = models.CharField(max_length=30)
    courses = models.ManyToManyField('Course', related_name='studentcourses')

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
