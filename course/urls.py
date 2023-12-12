# courses/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('all-courses/', views.all_courses, name='all_courses'),
    path('coursebycategory/<int:category_id>/', views.coursebycategory, name='course-by-category'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),

]
