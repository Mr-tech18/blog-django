from django.urls import path
from . import views

app_name="author_p" #author_p= author_page
urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('author_page/',views.author_page,name="author"),
    path('manage_comment/',views.post_comment,name="comment"),
    path('add_post/',views.add_post_author,name="add-post"),
    path('post_list/',views.post_list,name="post-list"),
    path('post_list_filter_ajax/',views.post_list_filter_ajax,name="category-post"),
    path('filter_comments/',views.auth_filter_comments_view_ajax,name="comments-filter"),
    path('edit_post/<post_id>/',views.edit_post,name="edit-post"),
    path('delete_post/<post_id>/',views.delete_post,name="delete-post"),
    path('edit_profile/',views.edit_profile,name="edit-profile"),
    path('auth-login/',views.auth_login_view,name="login"),
    path('auth-logout/',views.logout_view,name="logout"),
]
