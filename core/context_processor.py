from core.models import *

def general(request):
    categories=Category.objects.all()

    authors=Author.objects.filter(status=True)

    context={
        "categories":categories,
        "authors":authors,
    }

    return context