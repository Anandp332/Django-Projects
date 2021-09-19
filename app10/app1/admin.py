from django.contrib import admin
from app1.models import Employee,ContractEmployee,RegularEmployee
admin.site.register(Employee)
admin.site.register(RegularEmployee)
admin.site.register(ContractEmployee)
# Register your models here.
