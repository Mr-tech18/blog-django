from django.contrib.auth.backends import ModelBackend
from core.models import Author
from userauth.models import CustomUser

class AuthorAuthenticationEmail(ModelBackend):
    def authenticate(request,email=None,password=None,*kwargs):
        try:
            author=Author.objects.get(email=email)

            if author.check_password(password) and author.is_author:
                return author
        except Author.DoesNotExist:
            return None
        
class AuthorAuthenticationName(ModelBackend):
    def authenticate(request,name=None,password=None,*kwargs):
        try:
            author=Author.objects.get(name=name)

            if author.check_password(password) and author.is_author:
                return author
        except Author.DoesNotExist:
            return None
