from django.shortcuts import render,HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')
   #return HttpResponse("This is Homepage")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("This is aboutpage")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("This is a Service page")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        contact= Contact(name=name, email=email,phone=phone,date=datetime.today())
        contact.save()
        messages.success(request, "Profile details has been updated")
    return render(request,'contact.html')
    #return HttpResponse("This is a Contact page")