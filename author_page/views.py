from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth import authenticate,login
# Create your views here.





def add_post_author(request):
    data=render_to_string("async_auth/add_post.html")

    return JsonResponse({
        'context':data
    })
def post_comment(request):
    data=render_to_string("async_auth/comment.html")

    return JsonResponse({
        'context':data
    })
def dashboard(request):
    data=render_to_string("async_auth/dashboard.html")

    return JsonResponse({
        'context':data
    })
def edit_profile(request):
    data=render_to_string("async_auth/edit_profile.html")

    return JsonResponse({
        'context':data
    })

def edit_post(request):
    data=render_to_string("async_auth/edit_post.html")

    return JsonResponse({
        'context':data
    })

def author_page(request):
    author=request.author
    if author.is_authenticated:
        context={
            'author':author
        }
        return render(request,'authors_page.html',context)
    else:
        return redirect("author_p:login")


def  auth_login_view(request):

    email=None
    name=None
    if request.method=="POST":
        
        try:
            email=request.POST.get('email')
        except:
            name=request.POST.get('name')

            

        password=request.POST.get('password')
        if email is None:
            author=authenticate(name=name,password=password)
            print('login with name')
        else:
            author=authenticate(email=email,password=password)
            print('login with email...')

        if author is not None:
            login(request,author)
            return redirect('author_p:author')
    
    return render(request,'auth_login.html')