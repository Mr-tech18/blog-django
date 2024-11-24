from django.urls import path
from . import views

app_name="author_p" #author_p= author_page
urlpatterns = [
    path('dashboard',views.dashboard,name="dashboard"),
    path('author_page/',views.author_page,name="author"),
    path('manage_comment/',views.post_comment,name="comment"),
    path('add_post/',views.add_post_author,name="add-post"),
    path('edit_post/',views.edit_post,name="edit-post"),
    path('edit_profile/',views.edit_profile,name="edit-profile"),
    path('auth-login/',views.auth_login_view,name="login"),
    path('auth-logout/',views.logout_view,name="logout"),
]
