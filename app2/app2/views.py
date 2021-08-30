from django.shortcuts import render


def homev(request):
    return render(request,'home.html')
