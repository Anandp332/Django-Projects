from django.shortcuts import render


def homev(request):
    return render(request,'home.html')
def signin(request):
    return render(request,'signin.html')
def signup(request):
    return render(request,'signup.html')
