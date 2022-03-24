
from django.contrib import admin
from django.urls import path
from img_csv.views import profile_upload

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload_csv/', profile_upload , name = 'profile_upload'),
]
