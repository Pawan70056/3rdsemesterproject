from django.shortcuts import get_object_or_404, render

from .models import Course


def dashboard(request):
    return render(request, 'dashboard.html')




def all_courses(request):
    # Retrieve all courses from the database
    courses = Course.objects.all()
    return render(request, 'all_courses.html', {'courses': courses})

