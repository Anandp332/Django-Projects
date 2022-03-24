

from django.contrib import admin
from empdata.models import Employee,ContractEmployee,RegularEmployee,Address
admin.site.register(Employee)
admin.site.register(Address)
admin.site.register(RegularEmployee)
admin.site.register(ContractEmployee)
