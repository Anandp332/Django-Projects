from django.shortcuts import render
from django.core.mail import send_mail
from app18.settings import EMAIL_HOST_USER
from . import forms


def composemail(request):
    sub = forms.SubscribeForm()
    if (request.method == 'POST'):
        sub = forms.SubscribeForm(request.POST)
        subject = 'Mail for testing purpose'
        message = 'Hope you will Enjoy mail Sending Session'
        recepient = str(sub['Email'].value())
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
        return render(request, 'success.html', {'recepient': recepient})
    return render(request, 'index.html', {'form': sub})
