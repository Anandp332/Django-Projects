from django.shortcuts import render


def homev(request):
    return render(request,'home.html')
def signinv(request):
    return render(request,'signin.html')
def signupv(request):
    return render(request,'signup.html')
