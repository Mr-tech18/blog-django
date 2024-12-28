from django.urls import path

from . import views
app_name='otp_core'

urlpatterns = [
    path('', views.register, name='register'),
    path('home', views.home, name='home'),
    path('otp/<str:uid>/', views.otpVerify, name='otp_v')
]