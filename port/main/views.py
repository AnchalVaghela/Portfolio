from django.shortcuts import render
from .models import Contact
# Create your views here.

def index(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        sub = request.POST.get('sub')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.sub = sub
        contact.message = message
        contact.save()
    return render(request,'main/index.html')

def contact(request):
    return render(request,'main/contact.html')