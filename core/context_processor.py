from core.models import *

def general(request):
    categories=Category.objects.all()

    authors=Author.objects.filter(status=True)
    nb_categories=categories.count()
    context={
        "categories":categories,
        "authors":authors,
        "nb_categories":nb_categories
    }

    return context