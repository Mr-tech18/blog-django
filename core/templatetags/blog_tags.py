from django import template
from core.models import *


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

