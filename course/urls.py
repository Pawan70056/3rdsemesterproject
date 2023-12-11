# courses/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    # Endpoint to get all courses
    path('all-courses/', views.all_courses, name='all_courses'),
    path('subjets_details/', views.details, name='details'),

]
