
from django.contrib import admin
from django.urls import path
from send_mail.views import composemail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',composemail , name = 'composemail')
]
