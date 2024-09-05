from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post,Author,Category
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
                          'profile_image'
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


admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Author,AuthorAdmin)
