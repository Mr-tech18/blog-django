from .models import Comment,ContactUs,Author
from django import forms

class CommentForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput({'placeholder':"Your name"}))
    email=forms.CharField(widget=forms.EmailInput({'placeholder':"Your Email"}))
    content=forms.CharField(widget=forms.Textarea({f'placeholder':"Your comment goes here..."}))

    class Meta:
        model=Comment

        fields=['name','email','content']

 
class ContactUsForm(forms.ModelForm):
    whatsapp_number=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter your phone number ex:+237692109697"}))
    subject=forms.CharField(max_length=300)
    class Meta:
        model=ContactUs
        exclude=['date']

class AuthorForm(forms.ModelForm):
    #Name=forms.CharField(max_length=250,widget=forms.TextInput(attrs={'placeholder':"enter you email or your author name"}))
    class Meta:
        model=Author
        exclude=('agency_descript','rating','aid','author_image','status','user','is_author')