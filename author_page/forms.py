from django import forms
from core.models import Author,Post,Comment

class AuthorProfileEdit(forms.ModelForm):
    class Meta:
        model=Author
        exclude=('rating','aid','status','user','is_author')

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','description','content','status','reading_time','slug',"author",'category','profile_image']
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=["status"]