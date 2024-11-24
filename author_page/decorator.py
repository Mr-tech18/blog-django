from functools import wraps
from django.http import HttpResponseForbidden


def author_required(view_func):
    """
        this decorator ensure that some view are only accessed by authenticated author
    """
    @wraps(view_func)
    def _wrapped_view(request,*args,**kwargs):

        if not request.author or not request.author.is_authenticated:
            return HttpResponseForbidden(('Access forbidden , this page is only available for authenticated author'))
        return view_func(request,*args,*kwargs)
    return _wrapped_view