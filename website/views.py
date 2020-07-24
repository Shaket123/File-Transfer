from django.shortcuts import render
from django.http import FileResponse,HttpResponse
from .models import sender
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import math, random
import smtplib
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'website/index.html')

def send(request):
    return render(request,'website/send.html')

def recieve(request):
    return render(request,'website/recieve.html')

def about(request):
    return render(request,'website/about.html')

def contact(request):
    return render(request,'website/contact.html')

def sender_submit(request):
        digits='0123456789'
        otp=''
        for i in range(4):
            otp += digits[math.floor(random.random()*10)]

        se = request.POST["se"]
        re = request.POST["re"]
        fi = request.FILES['fi']
        #filename=fi.save(fi.name,fi)
        data = sender(sender_email=se, reciver_email=re, otp=otp ,file=fi)
        data.save()
        sendemail(otp,re)
        return render(request, 'website/index.html')


def sendemail(otp,re):
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("shaketmadandahiwale111@gmail.com", "Shaket@123")
    message = "your verification code to download file is  "+otp
    s.sendmail("shaketmadandahiwale111@gmail.com", re, message)
    s.quit()

def reciver_submit(request):

    si = request.POST["si"]
    ri = request.POST["ri"]
    otpi = request.POST["otpi"]
    try:
        a = sender.objects.get(sender_email = si)
    except:
       return render(request,'website/recieve.html')
    else:
        if (a.reciver_email == ri and a.otp == otpi):
            return render(request,'website/a.html',{"a":a})
        else:
            return render(request, 'website/recieve.html')














