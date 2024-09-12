from django.shortcuts import render,get_object_or_404
from .models import Post,Author,Category
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


def post_details(request,post_id,slug):
    post=get_object_or_404(Post,pid=post_id)

    context={
        'post':post
    }

    return render(request,'single.html',context)

def contact(request):
    return render(request,"contact.html")

def all_category(request):
    render(request,"category.html")

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