from django.urls import path
from . import views

app_name='core'

urlpatterns = [
    path('',views.home,name='home'),
    path('home/',views.index2,name='home2'),
    path('single/<slug:slug>/<post_id>/',views.post_details,name='details'),
    path('contact/',views.contact_us_view,name="contact"),
    path('category/',views.all_category,name="categories"),
    path('category/<cid>/',views.category_posts,name="posts_per_category"),
    path('author/<auth_id>/',views.author_views,name="author"),
    path('AboutUs/',views.about_us,name="about"),
    path('login-reauired/',views.redirection_page,name="redirection"),
    path('Become-writer/',views.become_author_view,name="author-register-form"),
    path('Search-result/s/',views.search_view,name="search"),

    #ajax
    path('reaxtion/<post_id>/',views.post_reaction_views_ajax,name="reaction_view"),
    path('ajax_comment/<post_id>/',views.ajax_comment,name="ajax_comment"),
]
