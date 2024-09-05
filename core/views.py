from django.shortcuts import render,get_object_or_404
from .models import Post,Author
# Create your views here.
def home(request):
    posts=Post.published.all()
    num_author=Author.objects.count()
    num_visits=request.session.get("num_visits",0)
    num_visits+=1
    request.session['num_visits']=num_visits

    context={
        'posts':posts,
        'num_visits':num_visits,
    }
    return render(request,'index.html',context)


def post_details(request,post_id,slug):
    post=get_object_or_404(Post,pid=post_id)

    context={
        'post':post
    }

    return render(request,'single.html',context)

