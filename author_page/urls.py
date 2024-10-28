from django.urls import path
from . import views

app_name="author_p" #author_p= author_page
urlpatterns = [
    path('dashboard/',views.dashboard,name="view"),
]
