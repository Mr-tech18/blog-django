from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from core.models import Author
from userauth.models import CustomUser

get_user_model=Author

class AuthorAuthenticationEmail(ModelBackend):
    def authenticate(request,email=None,password=None,*kwargs):
        try:
            author=get_user_model().objects.get(email=email)

            if author.check_password(password) and author.is_author:
                return author
        except get_user_model().DoesNotExist:
            return None
        
class AuthorAuthenticationName(ModelBackend):
    def authenticate(request,name=None,password=None,*kwargs):
        try:
            author=get_user_model().objects.get(name=name)

            if author.check_password(password) and author.is_author:
                return author
        except get_user_model().DoesNotExist:
            return None
