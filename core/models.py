from django.db import models
from userauth.models import CustomUser
import uuid
from django.utils import timezone
from django.utils.safestring import mark_safe
# Create your models here.

#choices

RATING=(

        (1,"🌟⭐⭐⭐⭐"),
        (2,'🌟🌟⭐⭐⭐'),
        (3,'🌟🌟🌟⭐⭐'),
        (4,'🌟🌟🌟🌟⭐'),
        (5,'🌟🌟🌟🌟🌟'),
)

    

def get_user_directory_path(instance,filename):
    return "{0}/{1}".format(instance.user,filename)

def uuid_id_generated(prefix='',lenght=10):
    str_uuid=str(uuid.uuid4()).replace('-','')
    return (prefix+str_uuid)[:lenght]



class Category(models.Model):
    cid=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True,editable=False)
    title=models.CharField(max_length=150)
    category_image=models.ImageField(upload_to='category',default="./static/assets/images/1.jpg")

    class Meta:
        verbose_name_plural="categories"

    def get_cat_image(self):
        return mark_safe(f'<img src={self.category_image.url} width="50" height="50"')
    
    def __str__(self):
        return self.title
    
class Author(models.Model):
    aid=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True,editable=False)
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    status=models.BooleanField(default=True)
    rating=models.CharField(max_length=2,choices=RATING,default=RATING[0][0],null=True,blank=True)
    bio=models.TextField(null=True,blank=True)
    author_image=models.ImageField(upload_to=get_user_directory_path,default="./static/assets/images/1.jpg")
    email=models.EmailField()

    def get_aut_image(self):
        return mark_safe(f"<img src='{self.author_image.url}' width='50px' height='50px'/>")
         

    def __str__(self):
         return "{}".format(self.user)

    
class Post(models.Model):
     
    class StatusChoices(models.TextChoices):
        DRAFT='DB','DRAFT'
        PUBLISH="PB","Published"

    class PublishedManager(models.Manager):
        def get_queryset(self) :
            return super().get_queryset().filter(status=Post.StatusChoices.PUBLISH)
     

    pid=models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4,editable=False)
    title=models.CharField(max_length=150)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.CharField(max_length=150)
    slug=models.SlugField(max_length=150)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    profile_image=models.ImageField(upload_to="post",default="./static/assets/images/2.jpg")
    content=models.TextField(null=True,blank=True)
    status=models.CharField(max_length=2,choices=StatusChoices,default=StatusChoices.DRAFT)
    likes=models.ManyToManyField(CustomUser,related_name='post_like')
    dislike=models.ManyToManyField(CustomUser,related_name='post_dislike')
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    reading_time=models.CharField(max_length=5,default='3 min',null=True)
    updated=models.DateTimeField(auto_now=True)
    Rating=models.IntegerField(choices=RATING,default=RATING[0][0],null=True,blank=True)
    is_premium=models.BooleanField(default=False)

    objects=models.Manager()
    published=PublishedManager()

    class Meta:
        ordering=["-publish","-created"]

    def __str__(self):
        return f'{self.title}'
     
    def get_post_image(self):
        return mark_safe(f"<img src='{self.profile_image.url}' width='50px' height='50px'/>")
         
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    name=models.CharField(max_length=90,null=False,blank=True)
    email=models.EmailField(null=False,blank=True)
    content=models.TextField(null=True,blank=True)
    status=models.BooleanField(default=True)
    comment_date=models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering=['-comment_date']
    
    def __str__(self):
        return f'{self.content} by {self.name}'