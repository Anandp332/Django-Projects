from django.conf.urls import url

from app5.views import homev,signin,signup

urlpatterns = [
    url(r'^$',homev,name='homel'),
    url(r'^home/$',homev,name='homel'),
    url(r'^signin/$',signin,name='signinl'),
    url(r'^signup/$',signup,name='signupl'),
]
