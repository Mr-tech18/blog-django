from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .models import CustomUser
# Create your views here.
def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            username=cd['username']
            email=cd['email']
            password1=cd['password1']
            password2=cd['password2']

            if password1!=password2:
                messages.error(request,"the password didn't match")
                return render(request,'userauths/register.html',{"form":form})
            if CustomUser.objects.filter(email=email):
                messages.warning(request,"This email already exist")
                return render(request,'userauths/register.html',{"form":form})
            if CustomUser.objects.filter(username=cd['username']):
                #here we're checking if the username enter by user already exist in the database
                messages.error(request,"The username is already taken")
                return render(request,'userauths/register.html',{"form":form})
            user=CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            messages.success(request,"your account have been successfully created")
            return redirect('core:home')
    else:
        form=RegisterForm()

    return render(request,"userauths/register.html",{"form":form})


def login_view(request):
    if request.method=="POST":

        email=request.POST.get("email")
        password=request.POST.get("password")

        if not CustomUser.objects.filter(email=email):# or CustomUser.objects.filter(username=username):
            messages.error(request,"The email you enter doesn't exist")
            return render(request,'userauths/login.html',{'form':LoginForm})
        user=authenticate(email=email,password=password)
        if user is  None:
            messages.error(request,"Incorrect password")
            return render(request,"userauths/login.html",{'form':LoginForm})
        else:
            login(request,user)
            messages.success(request,f"'{user.username}' You're logged in..")
            return redirect('core:home')
    return render(request,"userauths/login.html",{'form':LoginForm})

def logout_view(request):
    logout(request)
    messages.success(request,"You're successfully logged out")
    return redirect('userauths:login')