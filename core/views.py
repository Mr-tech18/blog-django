from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Author,Category,Comment
from .forms import CommentForm,ContactUsForm,AuthorForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from django.http import JsonResponse
from django.views import View
# Create your views here.
def home(request):
    posts=Post.published.all()
    #p_posts=Post.published.annotate(total_likes=Count('likes')).order_by('-total_likes',"-publish")
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
    similar_posts=Post.published.filter(category=post.category).annotate(post_count=Count('likes')).order_by('-post_count','-publish').exclude(pid=post_id)[:5]
    if request.method=="GET":
        if request.user.is_authenticated:
            user=request.user
            if post.likes.filter(id=user.id).exists():
                msg=True
                print(msg)
    context={
        "post":post,
        "comments":comments,
        "msg":msg,
        "similar_posts":similar_posts,
    }

    return render(request, 'single.html', context)


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

def contact_us_view(request):

    if request.method=="POST":
        print("post method...")
        form=ContactUsForm(data=request.POST)

        if form.is_valid():
            cd=form.cleaned_data
            if cd['whatsapp_number'].startswith('+'):
                phone_num=cd['whatsapp_number'].removeprefix('+')

                if not phone_num.isdigit():
                    messages.error(request,'Invalide phone number make sure to wirite it without space between number')
                    return redirect('core:contact')
                form.save()
                messages.success(request,"Your messages have been successfully send")
                return redirect('core:contact')
            elif not cd['whatsapp_number'].isdigit():
                    messages.error(request,'The phone number you enter is not valid')
                    return redirect('core:contact')
            else:
                form.save()
    form=ContactUsForm()

    return render(request,"contact.html",{"form":form})

@login_required
def become_author_view(request):
    form=AuthorForm(data=request.POST)
    if form.is_valid():
        if request.method=='POST':
            if Author.objects.filter(user=request.user).exists():
                messages.error(request,"You're already a writer")
                return redirect('core:home')
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            form=AuthorForm()

    return render(request,'userauths/become_writer.html',{"form":form})

def redirection_page(request):
    return render(request,"redirection.html")