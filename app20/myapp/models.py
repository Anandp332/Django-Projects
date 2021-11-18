from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="my_images")

    class Meta:
        db_table = 'image'


class Person(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='my_images')

    class Meta:
        db_table = 'person'
