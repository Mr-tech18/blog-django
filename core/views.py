from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Author,Category,Comment,PostView
from .forms import CommentForm,ContactUsForm,AuthorForm,NewsLetterForm
from .models import Newsletter
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.contrib import messages
from userauth.forms import EditProfileForm
from userauth.models import CustomUser
from django.db.models import Count,Value
from django.db.models import Q
from datetime import datetime
from django.urls import reverse
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank,TrigramSimilarity
from taggit.models import Tag

def home(request):
    current_date=datetime.now()
    current_month=current_date.month
    current_year=current_date.year

    current_posts=Post.published.filter(Q(publish__year=current_year)&Q(publish__month=current_month))
    tags=Tag.objects.all()
    
    if len(current_posts)>0:
        posts=current_posts
    else:
        posts=Post.published.all().order_by('-publish')
    print(f"there's {len(current_posts)} post for the month {current_year}")
    
    
    context={
        'posts':posts,
        "tags":tags
        #'num_visits':num_visits,
    }
    return render(request,'index.html',context)

def index2(request):
    posts=Post.published.all()
    """  num_author=Author.objects.count()
    num_visits=request.session.get("num_visits",0)
    num_visits+=1
    request.session['num_visits']=num_visits """
    tags=Tag.objects.all()
    context={
        'posts':posts,
        "tags":tags
    }
    return render(request,'index2.html',context)


def post_details(request, post_id, slug_val):
    post = get_object_or_404(Post, pid=post_id,slug=slug_val)
    comments= Comment.objects.filter(post=post,status=True)
    complete_uri=request.build_absolute_uri()
    msg=False
    similar_posts=Post.published.filter(category=post.category).annotate(post_count=Count('likes')).order_by('-post_count','-publish').exclude(pid=post_id)[:5]
    

    if request.user.is_authenticated:
        #use the authenticated user id to track the view
        if not PostView.objects.filter(post=post,user=request.user).exists():
            PostView.objects.create(post=post,user=request.user)
    else:
        session_id=request.session.session_key
        if not PostView.objects.filter(post=post,session_id=session_id):
            PostView.objects.create(post=post,session_id=session_id)

    #we request the session
    #session=request.session

    #if "post_views" not in session:
    #    session['post_views']={}
    #
    ##check if post have been viewed before
    #
    #if post_id not in session:
    #    post.view_num+=1
    #    post.save() 
    #    #add the 'pk' to the session 'post_veiws'
    #    #this part ensure that a num view can only be update one time
    #    session['post_views'][post_id]=True
    #
    if request.method=="GET":
        if request.user.is_authenticated:
            user=request.user
            if post.likes.filter(id=user.id).exists():
                msg=True
                print(msg)
    context={
        "complete_uri":complete_uri,
        "post":post,
        "comments":comments,
        "msg":msg,
        "similar_posts":similar_posts,
    }

    return render(request, 'single.html', context)

def faq_view(request):
    return render(request,'Faq.html')

def term_view(request):
    return render(request,'term.html')

def privacy_view(request):
    return render(request,"privacy.html")

def user_profile(request,username):
    context={
        'user':request.user
    }
    return render(request,"user_profile.html",context)
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
            
             # Use authenticated user's data
             name = request.user.username
             email = request.user.email
             content =request.POST['content']
             username=name
             user_val=request.user
             profile_image_value=user_val.profile_image.url    
         else:
             # Use the form's data for anonymous users
            
             name = request.POST['name']
             email = request.POST['email']
             content =request.POST['content']
             username=name
             user_val=None
             profile_image_value="data:image/jpeg;base64,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"
        # Save the comment
    
         Comment.objects.create(
         user=user_val,
         name=username,
         email=email,
         content=content,
         post=post
                )
    comments_count = Comment.objects.filter(post=post).count()
    context = {
        'comments_count':comments_count,
        'content':request.POST['content'],
        'user':username,
        'profile_image':profile_image_value

    }
    
    return JsonResponse(
        {
            "context":context
        }
    )


def author_views(request, auth_id):
    """
    Display the author's profile with their posts and categories associated with those posts.
    """
    author = get_object_or_404(Author, aid=auth_id)
    posts = Post.published.filter(author=author)
    
    # Get distinct category IDs associated with the author's posts
    category_ids = posts.values_list('category_id', flat=True).distinct()
    categories = Category.objects.filter(cid__in=category_ids)
    
    context = {
        'posts': posts,
        'author': author,
        'categories': categories,
    }

    return render(request, "about_authors.html", context)


def ajax_author_views(request, auth_id):
    """
    Filter posts by selected categories via AJAX for a specific author.
    """
    author = get_object_or_404(Author, aid=auth_id)
    posts = Post.published.filter(author=author)
    
    # Retrieve selected category IDs from the request
    selected_categories = request.GET.getlist('category[]')
   
    
    # Filter posts by selected categories, if any
    if selected_categories:
        posts = posts.filter(category__cid__in=selected_categories)
    
    # Render filtered posts to a string for AJAX response
    context_html = render_to_string('async/posts-filter.html', {'posts': posts})

    return JsonResponse({'context': context_html})

 
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

def search_view(request):
    query=request.GET.get('q')
    vector=SearchVector("content",weight="A")+SearchVector("title",weight="B")
    search_query=SearchQuery(query)
    if not query or query.strip()=='':
        posts=None
    else:
        posts=Post.published.annotate(
            rank=SearchRank(vector,search_query,normalization=Value(4)),
        ).filter(rank__gte=0.3).order_by('-rank')
        #posts=Post.published.annotate(similarity=TrigramSimilarity('content',query)).filter(similarity__gt=0.).order_by('-similarity')
    context={
        "query":query,
        "posts":posts,
    }

    return render(request,"search.html",context)

def edit_profile(request,user_id,username):
    user = request.user  
    if request.method == "POST":
        form = EditProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,f'you profile have been successfully update {user.username}')
            return redirect(reverse('core:edit-profile', args=[user.id,user.username]))
    else:
        form = EditProfileForm(instance=user)

   
    return render(request, 'edit_profile.html', {'form': form})



def newsletter_view(request):
    if request.method == "POST":
        form = NewsLetterForm(data=request.POST)
        email = request.POST.get('email')
        if form.is_valid():
            if Newsletter.objects.filter(email=email).exists():
              messages.error(request, "This email is already subscribed to our newsletter.")
              return redirect('core:home')
            form.save()
            messages.success(request, "You have successfully subscribed to our newsletter.")
        else:
            for error in form.errors.values():
                messages.error(request, error)
    return redirect('core:home')

def post_with_tags(request,tag_slug):
    """
        description:this class is used to retrieve all posts related to a single tags
        author:Mr_tech18@gmail.com
    """
    tag=get_object_or_404(Tag,slug=tag_slug)
    posts=Post.published.filter(tags__in=[tag])
    context={
        "posts":posts,
        "tag_name":tag.name

    }

    return render(request,"tags_result.html",context)




def custom_403_view(request, exception=None):
    return render(request, 'errors/403.html', status=403)

def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)
