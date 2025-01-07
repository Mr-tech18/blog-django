from django.urls import path
from . import views
from .feeds import LatestPostsFeed
# urls.py
from core.views import custom_403_view, custom_404_view
from django.conf.urls import handler403, handler404

handler403 = custom_403_view
handler404 = custom_404_view

app_name='core'

urlpatterns = [
    path('',views.home,name='home'),
    path('home/',views.index2,name='home2'),
    path('details/<slug:slug_val>/<post_id>/',views.post_details,name='details'),
    path('contact/',views.contact_us_view,name="contact"),
    path('category/',views.all_category,name="categories"),
    path('category/<cid>/',views.category_posts,name="posts_per_category"),
    path('author/<auth_id>/',views.author_views,name="author"),
    path('AboutUs/',views.about_us,name="about"),
    path('login-reauired/',views.redirection_page,name="redirection"),
    path('Become-writer/',views.become_author_view,name="author-register-form"),
    path('Search-result/s/',views.search_view,name="search"),
    path('FAQ/',views.faq_view,name='faq'),
    path('privacy/',views.privacy_view,name='privacy'),
    path('term and condition/',views.term_view,name='term'),
    path('user-profile/<str:username>',views.user_profile,name='profile_user'),
    path('feeds/',LatestPostsFeed(),name='posts_feed'),
    path('edit-profile/<user_id>/<username>',views.edit_profile,name='edit-profile'),
    path('newsletter/',views.newsletter_view,name='newsletter'),
    path('Search-result/tags/<tag_slug>/',views.post_with_tags,name="tag"),


    #ajax
    path('reaxtion/<post_id>/',views.post_reaction_views_ajax,name="reaction_view"),
    path('ajax_comment/<post_id>/',views.ajax_comment,name="ajax_comment"),
    path('ajax_author_views/<auth_id>/',views.ajax_author_views,name="ajax-author"),
]
