from django import template
from core.models import *
from django.db.models import Count
from django.db.models import F

register=template.Library()

@register.inclusion_tag("templates_tags/latest_post.html")
def show_latest_post(count=10):
    posts=Post.published.all().order_by('-publish')[:count]
    
    return {
        "posts": posts,
    }


@register.inclusion_tag('templates_tags/show_authors.html')
def show_author(count=3):
    authors=Author.objects.all()[:count]
    context={
        'authors':authors
    }

    return context


@register.simple_tag
def popular_post(count=10):
    posts=Post.published.annotate(total_likes=Count('likes'),comment_count=models.Count('comment')).order_by('-total_likes','-comment_count',"-publish")[:count]
    
    print("total posts",posts.count())
    return posts


@register.simple_tag
def top_author(count=5):
    authors=Author.objects.filter(status=True).annotate(top_author=models.Count('post')).order_by('-top_author')

    return authors