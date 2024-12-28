from django.db import models
from django.contrib.auth.models import User
from userauth.models import CustomUser
import uuid
# Create your models here.
def uuid_id_generated(prefix='',lenght=10):
    str_uuid=str(uuid.uuid4()).replace('-','')
    return (prefix+str_uuid)[:lenght]

class Profile(models.Model):
    user=models.OneToOneField(CustomUser,   on_delete=models.CASCADE,related_name="profile")
    phone_number=models.CharField(max_length=15)
    otp=models.CharField(max_length=100,null=True,blank=True)
    uid=models.CharField(default=uuid_id_generated('pr'),max_length=200)