from django.db import models

#One To One Relation
class Car(models.Model):
    reg_no = models.CharField(max_length=10)
    owner_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Car"
        db_table = 'car'

    def __str__(self):
        return self.reg_no


class Engine(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, primary_key=True)
    FuelType = models.CharField(max_length=100)
    Engine_year = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Engine'
        db_table = 'engine'

    def __str__(self):
        return str(self.Engine_year)
