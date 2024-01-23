from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.user_login , name='login'),
    path('register/', views.register, name='register' ),
     path('profile/', views.view_profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('settings/', views.settings,name = 'settings'),
    path('logout/', views.logout_view, name='logout_user'),

    # forget Password

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html'), name='reset_password'),
        
    path('reset_email_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),
      
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'), name='password_reset_confirm'),
      
    path('reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'), name='password_reset_complete'),
]
    
