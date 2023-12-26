import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Book, Chapter, Content, Course, CourseCategory, MyCourses


def dashboard(request):
    # Retrieve all course categories
    course_categories = CourseCategory.objects.all()
    
    # Pass course categories to the template context
    return render(request, 'dashboard.html', {'course_categories': course_categories})

def all_courses(request):
    # Fetch all courses or perform any necessary operations
    courses = Course.objects.all()  
    books = Book.objects.all()

    # Pass courses data to the template context
    context = {
        'courses': courses,
        'books': books
    }

    # Render the 'allCourses.html' template with the context
    return render(request, 'allCourses.html', context)


def coursebycategory(request, category_id):
    # Fetch the specific category using the category_id passed in the URL
    category = CourseCategory.objects.get(pk=category_id)

    # Retrieve all courses related to the specific category
    courses_in_category = Course.objects.filter(category=category)
    books = Book.objects.filter(category =category)
    context = {
        'courses_in_category': courses_in_category,
        'books': books,
        'category': category
    }
    # Pass the category and related courses to the template context
    return render(request, 'courseByCategory.html', context)


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courseDetails.html', {'course': course})


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


def get_chapter_content(request, chapter_id):
    try:
        chapter = Chapter.objects.get(pk=chapter_id)
        contents = Content.objects.filter(chapter=chapter)

        # Serializing text content and pdf file paths for the chapter
        serialized_contents = []
        for content in contents:
            serialized_content = {
                'content_type': content.content_type,
                'text_content': content.text_content if content.content_type == 'text' else None,
                'pdf_file': content.pdf_file.url if content.content_type == 'pdf' else None
            }
            serialized_contents.append(serialized_content)

        data = {
            'chapter_title': chapter.title,
            'contents': serialized_contents
        }
        # print(json.dumps(data, indent=4))  # Printing the JSON data

        return JsonResponse(data)
    except Chapter.DoesNotExist:
        return JsonResponse({'error': 'Chapter not found'}, status=404)



@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    user = request.user

    # Check if the user is already enrolled in the course
    if MyCourses.objects.filter(user=user, course=course).exists():
        return render(request, 'readCourse.html')

    # Enroll the user in the course
    MyCourses.objects.create(user=user, course=course)
    return render(request, 'readCourse.html')
    




