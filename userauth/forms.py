from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={"placeholder":"Username"}))
    email=forms.CharField(max_length=50,widget=forms.EmailInput(attrs={"placeholder":"Email"}))
    password1=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={"placeholder":"password"}))
    password2=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={"placeholder":"confirm password","style":"width:200px;"}))

class LoginForm(forms.Form):
    email=forms.CharField(max_length=50,widget=forms.EmailInput(attrs={"placeholder":"Email"}),help_text="Your email")
    password=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={"placeholder":"password"}),help_text="Your password")