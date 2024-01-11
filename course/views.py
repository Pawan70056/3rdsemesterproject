import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .froms import FeedbackForm
from .models import (Book, Chapter, Content, Course, CourseCategory, Feedback,
                     MyCourses, Ticket)


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

    messages.success(request, 'Content Fetched Successfully')
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
        messages.info(request, 'You are already enrolled in the above course, you can read.')
        return render(request, 'readCourse.html')

    # Enroll the user in the course
    MyCourses.objects.create(user=user, course=course)
    messages.success(request, 'You have successfully enrolled in the above course.')

    return render(request, 'readCourse.html')
    


@login_required
def my_courses(request):
    user = request.user
    enrolled_courses = MyCourses.objects.filter(user=user)
    return render(request, 'my_courses.html', {'enrolled_courses': enrolled_courses})


# feedback_reviews/views.py


@login_required
def feedback_submission(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            improvement_areas = request.POST.getlist('improvement_areas')  # Get the selected improvement areas from the form
            for area in improvement_areas:
                feedback.improvement_areas.add(area)
            feedback.save()
            messages.success(request, 'Feedback has been sent successfully')
            return redirect('dashboard')  # Redirect to a 'thank you' page after successful form submission
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})



def ticket(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback_type = request.POST.get('feedbackType')
        severity = request.POST.get('severity', '')  # Optional, may not be present if feedback_type is 'suggestion'
        message = request.POST.get('message')

        ticket = Ticket.objects.create(
            name=name,
            email=email,
            feedback_type=feedback_type,
            severity=severity,
            message=message
        )

        # Optionally, you can return a JSON response to indicate success
        messages.success(request, 'Ticket was created successfully')
        return redirect('dashboard')

    # If the request is not a POST request, render the form
    return render(request, 'ticket.html')
