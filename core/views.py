from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Author,Category,Comment
from .forms import CommentForm
from django.http import JsonResponse
# Create your views here.
def home(request):
    posts=Post.published.all()
    """    num_author=Author.objects.count()
    num_visits=request.session.get("num_visits",0)
    num_visits+=1
    request.session['num_visits']=num_visits """

    context={
        'posts':posts,
        #'num_visits':num_visits,
    }
    return render(request,'index.html',context)
def index2(request):
    posts=Post.published.all()
    """  num_author=Author.objects.count()
    num_visits=request.session.get("num_visits",0)
    num_visits+=1
    request.session['num_visits']=num_visits """

    context={
        'posts':posts,
        #'num_visits':num_visits,
    }
    return render(request,'index2.html',context)


def post_details(request, post_id, slug):
    post = get_object_or_404(Post, pid=post_id)
    comments= Comment.objects.filter(post=post)
    msg=False
    
    if request.method=="GET":
        if request.user.is_authenticated:
            user=request.user
            if post.likes.filter(id=user.id).exists():
                msg=True
                print(msg)
    context={
        "post":post,
        "comments":comments,
        "msg":msg
    }

    return render(request, 'single.html', context)

def contact(request):
    return render(request,"contact.html")


def category_posts(request,cid):
    """
        description:this class is used to retrieve all posts related to a single category
        author:Mr_tech18@gmail.com
    """
    posts=Post.published.filter(category__cid=cid)
    try:
        category=Category.objects.get(cid=cid)
    except:
        category=""
    context={
        "posts":posts,
        "category":category
    }

    return render(request,"single_post_category.html",context)


def ajax_comment(request,post_id):
    post = get_object_or_404(Post, pid=post_id)
    comment=None
    if request.method == "POST":
         if request.user.is_authenticated:
             print(f"User is authenticated: {request.user.username}")  # Debug print
             # Use authenticated user's data
             name = request.user.username
             email = request.user.email
         else:
             # Use the form's data for anonymous users
             print("Anonymous user!")  # Debug print
             name = request.POST['name']
             email = request.POST['email']
         
         content =request.POST['content']
         
         # Save the comment
         comment=Comment.objects.create(
             name=name,
             email=email,
             content=content,
             post=post
         )

    comments_count = Comment.objects.filter(post=post).count()
    context = {
        'comments_count':comments_count,
        'content':request.POST['content'],
        'user':comment.name,

    }
    
    return JsonResponse(
        {
            "context":context
        }
    )

def author_views(request,auth_id):
    author=get_object_or_404(Author,aid=auth_id)
    posts=Post.published.filter(author__aid=author.aid)
    context={
        'posts':posts,
        'author':author,
    }

    return render(request,"about_authors.html",context)

def all_category(request):
    categories=Category.objects.all()

    return render(request,'category.html',{"categories":categories})


def about_us(request):
    return render(request,'about_us.html')




def post_reaction_views_ajax(request,post_id):
    post=get_object_or_404(Post,pid=post_id)

    msg=False
    
    if request.method=="POST":

        if request.user.is_authenticated:
            user=request.user
            if post.likes.filter(id=user.id).exists():
                post.likes.remove(user)
                msg=False
                print(msg)
            else:
                post.likes.add(user)
                msg=True
    
    context={
        'like_number':post.likes.count(),
        "msg":msg,
    }
    return JsonResponse({
        'context':context,
    })