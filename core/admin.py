from django.contrib import admin
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string

from django.utils.html import strip_tags


from .models import *
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','author','get_post_image','status','category']
    search_fields=['title','content']
    prepopulated_fields={'slug':['title',],}
    ordering=['status','-publish']

    fieldsets=(
        (
            'General',{
                'classes':['collapse',],
                'fields':('title','author','status','category','tags',
                          'slug','description','publish','reading_time',
                          'profile_image','likes'
                          )
            }
        ),
        (
            'Blog post',{
                'description':"Post content",
                'fields':('content',),
            }
        ),
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display=['get_cat_image','title']

class AuthorAdmin(admin.ModelAdmin):
    list_display=['user','email','status','get_aut_image']
    search_fields=['user','email']

class CommentAdmin(admin.ModelAdmin):
    list_display=['name','post','email']


class AdminContactUs(admin.ModelAdmin):
    list_display=['name','subject','date']


class PostViewAdmin(admin.ModelAdmin):
    list_display=['post','user','session_id']


def send_custom_email_to_users(modeladmin, request, queryset):
    for user in queryset:
        # Render the HTML email template with user-specific context
        html_content = render_to_string('news.html')
        text_content = strip_tags(html_content)  # Fallback text content

        # Create an email message with plain text and HTML content
        email = EmailMultiAlternatives(
            subject='Welcome!',
            body=text_content,
            from_email='techgroupe18@gmail.com',
            to=[user.email],
        )

        # Attach the HTML version
        email.attach_alternative(html_content, "text/html")
        email.send(fail_silently=False)

    modeladmin.message_user(request, "Custom emails sent successfully!")

send_custom_email_to_users.short_description = "Send customized email to selected users"

class NewsletterAdmin(admin.ModelAdmin):
    list_display=['email','date']
    actions = [send_custom_email_to_users]


admin.site.register(Newsletter,NewsletterAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(ContactUs,AdminContactUs)
admin.site.register(PostView,PostViewAdmin)



