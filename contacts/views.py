from django.shortcuts import render , redirect

# Create your views here.
from .models import Contact

def send_message(request):

    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    phone = request.POST['phone']
    message = request.POST['message']

    contact = Contact(name=name,email=email,subject=subject,phone=phone,message=message)
    print("contact saved")
    contact.save()

    return redirect("/")

