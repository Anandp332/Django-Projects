from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from app1.views import index,insertBooks
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'$^',index),
    url(r'save',insertBooks)
]
