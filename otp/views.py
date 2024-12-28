from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from userauth.models import CustomUser
from .models import Profile
import random
from .helper import MessageHandler

def home(request):
    if request.COOKIES.get('verified') and request.COOKIES.get('verified')!=None:
        return HttpResponse(" verified.")
    else:
        return HttpResponse(" Not verified.")
    

def register(request):
    if request.method=="POST":
        if CustomUser.objects.filter(username__iexact=request.POST['user_name']).exists():
            return HttpResponse("User already exists")

        user=CustomUser.objects.create(username=request.POST['user_name'])
        otp=random.randint(1000,9999)
        profile=Profile.objects.create(user=user,phone_number=request.POST['phone_number'],otp=f'{otp}')
        if request.POST['methodOtp']=="methodOtpWhatsapp":
            messagehandler=MessageHandler(request.POST['phone_number'],otp).send_otp_via_whatsapp()
        else:
            messagehandler=MessageHandler(request.POST['phone_number'],otp).send_otp_via_message()
        red=redirect(reverse('otp_core:otp_v',args=[f"{profile.uid}"]))
        red.set_cookie("can_otp_enter",True,max_age=600)
        return red  
    return render(request, 'otp/register.html')

def otpVerify(request,uid):
    if request.method=="POST":
        profile=Profile.objects.get(uid=uid)     
        if request.COOKIES.get('can_otp_enter')!=None:
            if(profile.otp==request.POST['otp']):
                red=redirect("otp_core:home")
                red.set_cookie('verified',True)
                return red
            return HttpResponse("wrong otp")
        return HttpResponse("10 minutes passed")        
    return render(request,"otp/otp.html",{'id':uid})