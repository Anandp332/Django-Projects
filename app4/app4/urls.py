from django.conf.urls import url

from .view import homev,signinv,signupv
urlpatterns = [
    url(r'^$',homev,name='homel'),
    url(r'^signin/$',signinv,name='signinl'),
    url(r'^signup/$',signupv,name='signupl'),
    url(r'^home/$',homev,name='homel'),

]
