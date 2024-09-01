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

class CategoryAdmin(admin.ModelAdmin):
    list_display=['cid','get_cat_image','title']

class AuthorAdmin(admin.ModelAdmin):
    list_display=['aid','name','email','status','get_aut_image']
    search_fields=['name','email']

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Author,AuthorAdmin)