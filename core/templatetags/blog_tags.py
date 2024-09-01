from django import template
from core.models import Post


register=template.Library()

@register.inclusion_tag("templates_tags/latest_post.html")
def show_latest_post(count=10):
    posts=Post.published.all().order_by('-publish')[:count]
    
    return {
        "posts": posts,
    }
