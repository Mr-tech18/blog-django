from core.models import *

def general(request):
    categories=Category.objects.all()

    context={
        "categories":categories
    }

    return context