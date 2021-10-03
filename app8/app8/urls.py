from django.conf.urls import url
from emp.views import homev

urlpatterns = [
    url(r'$^',homev ,name='homel')
]
