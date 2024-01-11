# courses/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('all-courses/', views.all_courses, name='all_courses'),
    path('coursebycategory/<int:category_id>/', views.coursebycategory, name='course-by-category'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),
    path('read/<int:course_id>/', views.read, name= "read"),
    path('get_chapter_content/<int:chapter_id>/', views.get_chapter_content, name='get_chapter_content'),
    path('my-courses/', views.my_courses, name='my_courses'),
    path('feedback/', views.feedback_submission, name='feedback_submission'),
    path('ticket/', views.ticket, name='ticket'),
    path('contact/', views.contact_view, name='contact'),


]
