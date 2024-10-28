from .models import Comment,ContactUs
from django import forms

class CommentForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput({'placeholder':"Your name"}))
    email=forms.CharField(widget=forms.EmailInput({'placeholder':"Your Email"}))
    content=forms.CharField(widget=forms.Textarea({f'placeholder':"Your comment goes here..."}))

    class Meta:
        model=Comment

        fields=['name','email','content']

 
class ContactUsForm(forms.ModelForm):
    class Meta:
        model=ContactUs
        exclude=['date']
     