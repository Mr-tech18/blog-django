from django.urls import path
from . import views

app_name='core'

urlpatterns = [
    path('home/',views.home,name='home'),
    path('home/',views.index2,name='home2'),
    path('home/<slug:slug>/<post_id>/',views.post_details,name='details'),
    path('contact/',views.contact,name="contact"),
    path('category/',views.all_category,name="categories"),
    path('category/<cid>/',views.category_posts,name="posts_per_category"),
]
