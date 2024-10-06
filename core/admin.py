from django.contrib import admin


from .models import *
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','author','get_post_image','status','category']
    search_fields=['title','content']
    prepopulated_fields={'slug':['title',],}
    ordering=['status','-publish']

    fieldsets=(
        (
            'General',{
                'classes':['collapse',],
                'fields':('title','author','status','category',
                          'slug','description','publish','reading_time',
                          'profile_image','likes'
                          )
            }
        ),
        (
            'Blog post',{
                'description':"Post content",
                'fields':('content',),
            }
        ),
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display=['get_cat_image','title']

class AuthorAdmin(admin.ModelAdmin):
    list_display=['user','email','status','get_aut_image']
    search_fields=['user','email']

class CommentAdmin(admin.ModelAdmin):
    list_display=['name','post','email']

admin.site.register(Comment,CommentAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Author,AuthorAdmin)
