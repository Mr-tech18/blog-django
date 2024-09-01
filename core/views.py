from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.
def home(request):
    posts=Post.published.all()

    context={
        'posts':posts,
    }
    return render(request,'index.html',context)


def post_details(request,post_id,slug):
    post=get_object_or_404(Post,pid=post_id)

    context={
        'post':post
    }

    return render(request,'single.html',context)