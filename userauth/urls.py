from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name="userauths"

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('user_profile/',views.user_profile_veiw,name='user-profile'),
    path('reset-password/',auth_views.PasswordResetView.as_view(),name='password-reset'),
    path('reset-password/done/',auth_views.PasswordResetDoneView.as_view(),name='password-reset-done'),
    path('reset-password/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password-reset-confirm'),
    path('reset-password/complete/',auth_views.PasswordResetCompleteView.as_view(),name='password-reset-complete'),
]
