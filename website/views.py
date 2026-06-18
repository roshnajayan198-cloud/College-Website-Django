from django.shortcuts import render
from .models import Contact

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def courses(request):
    return render(request,"courses.html")


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

from django.shortcuts import render
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        messages.success(request, "Form submitted successfully. Thanks for your application!")

    return render(request, "contact.html")
