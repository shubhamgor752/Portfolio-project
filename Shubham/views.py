import json

# import requests
from django.shortcuts import render

from .models import Contact


def index(request):
    return render(request, 'mysite/index.html')


def portfolio(request):
    return render(request, 'mysite/portfolio.html')


def contact(request):
    if request.method=="POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phonenumber=request.POST['phonenumber'],
            address=request.POST['address']
            )
        msg="Contact Saved Succesfully"
        return render(request,'mysite/contact.html',{'msg':msg,})
    else:
        return render(request, 'mysite/contact.html')
