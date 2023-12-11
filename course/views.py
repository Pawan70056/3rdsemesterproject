from django.shortcuts import get_object_or_404, render

from .models import Course


def dashboard(request):
    return render(request, 'dashboard.html')

def all_courses(request):
     return render(request, 'law.html')

def details(request):
     return render (request, 'subject_overview.html')


