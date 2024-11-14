from django.utils.deprecation import MiddlewareMixin
from core.models import Author
from userauth.models import CustomUser
from django.shortcuts import redirect

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
        if request.user.is_authenticated:
            try:
                request.author=Author.objects.get(user=request.user)
            except Author.DoesNotExist:
                request.author=None
        else:
            request.author=None
        return self.get_response(request)
