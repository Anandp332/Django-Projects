from django.conf.urls import include, url


from .views import homev
urlpatterns = [
    url(r'^$',homev),
]
