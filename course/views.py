from django.shortcuts import get_object_or_404, render

from .models import Course, CourseCategory


def dashboard(request):
    # Retrieve all course categories
    course_categories = CourseCategory.objects.all()
    
    # Pass course categories to the template context
    return render(request, 'dashboard.html', {'course_categories': course_categories})




def all_courses(request):
    # Fetch all courses or perform any necessary operations
    courses = Course.objects.all()  # Example: Fetching all courses from the database

    # Pass courses data to the template context
    context = {
        'courses': courses,
    }

    # Render the 'allCourses.html' template with the context
    return render(request, 'allCourses.html', context)





def coursebycategory(request, category_id):
    # Fetch the specific category using the category_id passed in the URL
    category = CourseCategory.objects.get(pk=category_id)

    # Retrieve all courses related to the specific category
    courses_in_category = Course.objects.filter(category=category)

    # Pass the category and related courses to the template context
    return render(request, 'courseByCategory.html', {'category': category, 'courses_in_category': courses_in_category})


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courseDetails.html', {'course': course})

def enroll(request,course_id):
    pass




from django.shortcuts import render, get_object_or_404
from .models import Course

def read(request, course_id):
    # Retrieve the specific course based on course_id
    course = get_object_or_404(Course, pk=course_id)
    
    # Retrieve all chapters related to the course and their content
    chapters = course.chapters.all()
    chapter_contents = {}
    
    for chapter in chapters:
        chapter_contents[chapter] = chapter.contents.all()

    # Render the content of the course in a template
    return render(request, 'readCourse.html', {'course': course, 'chapters': chapters, 'chapter_contents': chapter_contents})


