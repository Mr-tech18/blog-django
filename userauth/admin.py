from email.mime.image import MIMEImage
from django.contrib import admin
from .models import CustomUser
# Register your models here.
from django.core.mail import send_mail
from .models import CustomUser

# admin.py

from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string

from django.utils.html import strip_tags

def send_custom_email_to_users(modeladmin, request, queryset):
    for user in queryset:
        # Render the HTML email template with user-specific context
        html_content = render_to_string('email_test.html', {'user': user})
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
        
        # Attach an inline image (logo or other image)
      
        """  with open('C:/Users/RBK/Desktop/django_english/blogprj/media\Mr_tech18/_4236cb4c-96e9-426f-90d9-41cae1adabb7.jpeg', 'rb') as img_file:
            image = MIMEImage(img_file.read())
            image.add_header('Content-ID', '<unique_image_id>')
            email.attach(image)
        """
        email.send(fail_silently=False)

    modeladmin.message_user(request, "Custom emails sent successfully!")

send_custom_email_to_users.short_description = "Send customized email to selected users"



class AdminUser(admin.ModelAdmin):
    list_display=['username',"email","get_profile_image","profile_image"]
    actions = [send_custom_email_to_users]

class CommentAdmin(admin.ModelAdmin):
    list_display=['name','post','email']


admin.site.register(CustomUser,AdminUser)


    
