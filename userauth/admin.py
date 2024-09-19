from django.contrib import admin
from .models import CustomUser
# Register your models here.
class AdminUser(admin.ModelAdmin):
    list_display=['username',"email","get_profile_image","profile_image"]

class CommentAdmin(admin.ModelAdmin):
    list_display=['name','post','email']


admin.site.register(CustomUser,AdminUser)