from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.


def dashboard(request):
    return render(request,'dashboard.html')

def login_author(request):
    user=request.user

    if not user.is_authenticated:
        return redirect('core:login_authors')
    
