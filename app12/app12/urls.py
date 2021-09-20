from django.contrib import admin
from django.urls import path
from Hostel_management_system import views


urlpatterns = [    
    path('admin/', admin.site.urls), # automatically created by django
    path('', views.home, name='register'), # when someone will access www.yourpage.com/ it will send request to 'home' view
    path('reg_form/', views.register, name='reg_form'),
    path('login/', views.user_login, name='login'),
    #path('hostels/<slug:hostel_name>/', views.hostel_detail_view, name='hostel'),
    path('login/edit/', views.edit, name='edit'),
    path('login/select/', views.select, name='select'),
    #path('logout/', views.logout_view, name='logout'),
    path('reg_form/login/edit/', views.edit, name='update'),
]
