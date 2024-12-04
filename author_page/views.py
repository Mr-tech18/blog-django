from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.http import JsonResponse
from core.models import Author,Post,Comment,Category
from .decorator import author_required
from django.contrib.auth import authenticate,login,logout
from .forms import AuthorProfileEdit,PostForm
from core.views import ajax_author_views
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

def get_comment_per_author(request):
    author=request.author
    posts=Post.published.filter(author=author)
    posts_ids=Post.published.filter(author=author).values_list('pid',flat=True)
    comments=Comment.objects.filter(post__pid__in=posts_ids)

    context={
        'comments':comments,
        "posts":posts,
        "author":author,
    }

    return context

def post_comment(request):
    
    context=get_comment_per_author(request)

    data=render_to_string("async_auth/comment.html",context,request)

    return JsonResponse({
        'context':data
    })

def auth_filter_comments_view_ajax(request):
    

    selected_posts=request.GET.getlist('post[]')#we retrieve the list of post_ids send trought ajax

    if selected_posts:
        comments=Comment.objects.filter(post__pid__in=selected_posts)
        context={
        "comments":comments,
    }
    else:
       context=get_comment_per_author(request)
    
    data=render_to_string("async_auth/post_table.html",context,request)

    return JsonResponse({
        'context':data
    })

def get_posts_by_author(request):
    """
        author:franck detagne
        we use this function to retrieve all post write by an author ,
        this view also retrieve all the category of posts written by the current logged in author
    """
    author=request.author
    posts=Post.objects.filter(author=author).order_by("-publish","-updated")
    post_category_ids=posts.values_list('category_id',flat=True)
    categories=Category.objects.filter(cid__in=post_category_ids)
    context={
        'posts':posts,
        'categories':categories
        }
    return context


def post_list(request):
    """
        this function just retrieve the value of the get_posts_by_author()
        and pass it to the render_to_string() who use the context dictionnary to render a html page 
        and then convert the result as a string , asign it variable , this variable is then used by js to render the content dynamically 
        the function responsable to send data to 'js' is jsonResponse()
    """
    context=get_posts_by_author(request)
    data=render_to_string('async_auth/auth_post_list.html',context,request)

    return JsonResponse({
        'context':data,
    })

def post_list_filter_ajax(request):
    selected_category=request.GET.getlist('category[]')#we retrieve the list of post_ids send trought ajax

    if selected_category:
        author=request.author
        posts=Post.objects.filter(author=author,category__cid__in=selected_category)
        context={
        "posts":posts,
    }
        data=render_to_string("async_auth/table_post_ajax.html",context,request)

    else:
       print('nohting...')
       context=get_posts_by_author(request)
       data=render_to_string("async_auth/table_post_ajax.html",context,request)

    return JsonResponse({
        'context':data
    })

def dashboard(request):
    data=render_to_string("async_auth/dashboard.html")

    return JsonResponse({
        'context':data
    })


def delete_post(request,post_id):
    post=Post.objects.get(pid=post_id)
    messages.success(request,f'{post.title}  have been successfull deleted')
    post.delete()

    return redirect('author_p:author')

def edit_post(request,post_id):
    
    post=Post.objects.get(pid=post_id)
    if request.method=="POST":
        form=PostForm(data=request.POST,files=request.FILES,instance=post)
        if form.is_valid():
            form.save()
            print(request.FILES)
            messages.success(request,"Your update are saved")
            return redirect('author_p:author')
        else:
            print(form.errors)
            print('the form is not valid..')
    else:
        form=PostForm(instance=post)
    context={
        "post":post,
        "form":form,
    }
    data=render_to_string("async_auth/auth_post_edit.html",context,request)
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


