from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe
# Create your models here.

def get_user_directory_path(instance,filename):
    return "{0}/{1}".format(instance.username,filename)

class CustomUser(AbstractUser):
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=50)
    profile_image=models.ImageField(upload_to=get_user_directory_path,null=True,blank=True,default="defaults/default.webp")

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username']

    def get_profile_image(self):
        return mark_safe("<img src='{0}' width='50' height='50' />".format(self.profile_image.url))
    
    def __str__(self):
        return f'{self.username}'