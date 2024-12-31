from django.db.models.base import Model
from django.utils.safestring import SafeText
import markdown
from .models import Post
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy


class LatestPostsFeed(Feed):
    title='ATAIN blogging'
    link=reverse_lazy('core:home')
    description='New posts of ATAIN blogging'

    def items(self):
        return Post.published.order_by('-publish')[:10]
    def item_title(self, item):
        return item.title
        
    def item_description(self, item: Model) :
        return truncatewords_html(markdown.markdown(item.content),30)
    
    def item_pubdate(self,item):
        return item.publish