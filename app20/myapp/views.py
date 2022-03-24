from django.shortcuts import render, redirect
from myapp import forms
from .models import Person


def insert(request):
    if (request.method == 'POST'):
        form = forms.PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        form = forms.PersonForm()
    return render(request, 'home.html', {'form': form})


def show(request):
    if request.method == 'GET':
        person = Person.objects.all()
        return render(request, 'showdata.html', {'person': person})
