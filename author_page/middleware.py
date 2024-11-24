from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from core.models import Author
from django.contrib.auth import get_user_model
from userauth.models import CustomUser
from django.shortcuts import redirect

get_user_model=Author

def get_current_author(request):
    if request.user.is_authenticated and hasattr(request.user,'author_profile'):
        return request.user.author_profile

class AuthorMiddleware(MiddlewareMixin):
    def process_request(self,request):
        try:
            user=request.user
            if user is None:
                 return redirect ('author_p:login')
        except CustomUser.DoesNotExist:
            return redirect('userauths:register')
        if request.user.is_authenticated:
            try:
                request.author=Author.objects.get(user=request.user)
            except Author.DoesNotExist:
                return redirect('core:home')
        else:
            return redirect('userauths:login')
        
        return None

class AuthorMiddleware1:

    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self,request):
        request.author=SimpleLazyObject(lambda:get_current_author(request))
        return self.get_response(request)
