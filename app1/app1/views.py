from django.http import HttpResponse


def homev(request):
    return HttpResponse('<h1>hello</h1>')
