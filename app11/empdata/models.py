from django.db import models
GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)
class Address(models.Model):
    flatno = models.CharField(max_length=10)
    appartment_name = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    def __str__(self):
        return self.city+ "," + self.state
    class Meta:
        verbose_name_plural = 'Address'
        db_table = 'address'
class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.IntegerField(choices=GENDER_CHOICES)
    address = models.ForeignKey('Address' , on_delete=models.CASCADE,)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Employee"
        db_table = 'employee'
class RegularEmployee(Employee):
    salary = models.IntegerField()
    bonus = models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "RegularEmployee"
        db_table = 'regularemployee'
class ContractEmployee(Employee):
    payperhour = models.IntegerField()
    duration = models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'ContractEmployee'
        db_table = 'contractemployee'

