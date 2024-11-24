from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.http import JsonResponse
from core.models import Author,Post
from .decorator import author_required
from django.contrib.auth import authenticate,login,logout
from .forms import AuthorProfileEdit,PostForm
# Create your views here.





def add_post_author(request):

    if request.method=="POST":
        form=PostForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print(request.FILES)
            messages.success(request,"Your post have been successfully created")
            return redirect('author_p:author')
        else:
            print(form.errors)
            print('the form is not valid..')
    else:
        form=PostForm()
    
    data=render_to_string("async_auth/add_post.html",{"form":form},request)
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
def edit_post(request):
    data=render_to_string("async_auth/edit_post.html")

    return JsonResponse({
        'context':data
    })


def edit_profile(request):
    print('profile edition view..')
    author = request.author  # Assuming middleware sets request.author

    if request.method == "POST":
        print('post...')
        form = AuthorProfileEdit(data=request.POST, files=request.FILES, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request,f'you profile have been successfully update {request.author.name}')
            return redirect("author_p:author")
    else:
        form = AuthorProfileEdit(instance=author)
        print('get...')

    data = render_to_string("async_auth/edit_profile.html", {'form': form}, request)
    return JsonResponse({'context': data})



@author_required
def author_page(request):
    author=request.author
    if author.is_authenticated:
        posts=Post.published.filter(author=author)
        context={
            'posts':posts,
            'author':author
        }
        return render(request,'authors_page.html',context)
    else:
        return redirect("author_p:login")


def  auth_login_view(request):

    email=None

    if request.method=="POST":
        
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        
        author=authenticate(email=email,password=password)

        if author is not None:
            login(request,author)
            return redirect('author_p:author')
        else:
            messages.error(request,"Your email or password is not valid")
            return redirect('author_p:login')
    
    return render(request,'auth_login.html')


def logout_view(request):
    logout(request)

    return redirect('author_p:login')