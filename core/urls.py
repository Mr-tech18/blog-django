from django.urls import path
from . import views

app_name='core'

urlpatterns = [
    path('home/',views.home,name='home'),
    path('home/<slug:slug>/<post_id>',views.post_details,name='details'),
]
