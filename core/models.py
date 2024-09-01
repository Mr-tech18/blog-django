from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone
# Create your models here.

#choices

RATING=(

        (1,"🌟⭐⭐⭐⭐"),
        (2,'🌟🌟⭐⭐⭐'),
        (3,'🌟🌟🌟⭐⭐'),
        (4,'🌟🌟🌟🌟⭐'),
        (5,'🌟🌟🌟🌟🌟'),
)

    

def get_user_directory_path(user,filename):
    return f"{0}/{1}".format(user.username,filename)

def uuid_id_generated(prefix='',lenght=10):
    str_uuid=str(uuid.uuid4()).replace('-','')
    return (prefix+str_uuid)[:lenght]



class Category(models.Model):
    cid=models.UUIDField(primary_key=True,default=uuid_id_generated('cat',10),unique=True)
    title=models.CharField(max_length=150)
    category_image=models.ImageField(upload_to=get_user_directory_path,default="./static/assets/images/1.jpg")

    class Meta:
        verbose_name_plural="categories"

    def get_cat_image(self):
        return f'<img src={self.category_image.url} width="50" height="50"'
    
    def __str__(self):
        return self.title
    
class Author(models.Model):
    cid=models.UUIDField(primary_key=True,default=uuid_id_generated('cat',10),unique=True)
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.BooleanField(default=True)
    rating=models.CharField(max_length=2,choices=RATING,default=RATING[0][0])
    bio=models.TextField(null=True,blank=True)
    author_image=models.ImageField(upload_to=get_user_directory_path,default="./static/assets/images/1.jpg")

    def get_cat_image(self):
        return f'<img src={self.author_image.url} width="50" height="50"'
         

    def __str__(self):
         return "{}".format(self.name)

    
class Post(models.Model):
     
    class StatusChoices(models.TextChoices):
        DRAFT='DB','DRAFT'
        PUBLISH="PB","Published"

    class PublishedManager(models.Manager):
        def get_queryset(self) :
            return super().get_queryset().filter(Post.StatusChoices.PUBLISH)
     

    pid=models.UUIDField(primary_key=True,unique=True,default=uuid_id_generated('pos',15))
    title=models.CharField(max_length=150)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.CharField(max_length=150)
    slug=models.SlugField(max_length=150)
    profile_image=models.ImageField(upload_to=get_user_directory_path,default="./static/assets/images/2.jpg")
    content=models.TextField(null=True,blank=True)
    status=models.BooleanField(default=True)
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    Rating=models.IntegerField(choices=RATING,default=RATING[0][0])
    is_premium=models.BooleanField(default=False)

    objects=models.Manager()
    published=PublishedManager()

    class Meta:
        ordering=["-publish","-created"]

    def __str__(self):
        return f'{self.title}'
     
