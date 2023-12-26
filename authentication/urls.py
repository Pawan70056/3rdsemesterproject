from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.user_login , name='login'),
    path('register/', views.register, name='register' ),
     path('profile/', views.view_profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('logout/', views.logout_view, name='logout'),
]
    
