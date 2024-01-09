from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class CourseCategory(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextField()
    thumbnail = models.ImageField()

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)
    description =RichTextField()
    thumbnail = models.ImageField()
    instructor = models.CharField(max_length=50)
    category = models.ForeignKey(CourseCategory, related_name='courses', on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Chapter(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, related_name='chapters', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Content(models.Model):
    TEXT = 'text'
    PDF = 'pdf'

    CONTENT_TYPE_CHOICES = [
        (TEXT, _('Text')),
        (PDF, _('PDF')),
    ]

    content_type = models.CharField(
        max_length=4,
        choices=CONTENT_TYPE_CHOICES,
        default=TEXT,
    )
    text_content = RichTextField(blank=True, null=True)
    pdf_file = models.FileField(upload_to='pdf_contents/', blank=True, null=True)
    chapter = models.ForeignKey(Chapter, related_name='contents', on_delete=models.CASCADE)

    def __str__(self):
        return f"Content of {self.chapter.title}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    category =models.ForeignKey(CourseCategory,on_delete=models.CASCADE)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    
    def __str__(self):
        return self.title



class MyCourses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"



class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    employment_status_choices = [
        ('student', 'Student'),
        ('job-full', 'Employed Full Time'),
        ('job-part', 'Employed Part Time'),
        ('self-employed', 'Self-employed'),
        ('unemployed', 'Unemployed'),
        ('retired', 'Retired'),
        ('preferNo', 'Prefer not to say'),
        ('other', 'Other')
    ]
    employment_status = models.CharField(max_length=20, choices=employment_status_choices)
    experience_level_choices = [
        ('junior', 'Junior (0-2 years experience)'),
        ('mid', 'Mid-level (2+ years experience)'),
        ('senior', 'Senior'),
        ('executive', 'Executive'),
        ('other', 'Other')
    ]
    experience_level = models.CharField(max_length=20, choices=experience_level_choices)
    course_rating_choices = [
        ('excellent', 'Excellent'),
        ('very-good', 'Very good'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor')
    ]
    course_rating = models.CharField(max_length=20, choices=course_rating_choices)
    materials_rating_choices = [
        ('extremely', 'Extremely useful'),
        ('very', 'Very useful'),
        ('somewhat', 'Somewhat useful'),
        ('not-so', 'Not so useful'),
        ('no', 'No useful at all')
    ]
    materials_rating = models.CharField(max_length=20, choices=materials_rating_choices)
    recommend_choices = [
        ('definitely', 'Definitely'),
        ('maybe', 'Maybe'),
        ('not-sure', 'Not sure')
    ]
    recommend_course = models.CharField(max_length=20, choices=recommend_choices)
    improvement_areas_choices = [
        ('lectures', 'Lectures and videos'),
        ('material', 'Instructional materials i.e. readings'),
        ('assignments', 'Course assignments and projects'),
        ('exams', 'Graded assignments and exams'),
        ('forum', 'Forum'),
        ('additional-courses', 'Additional Courses')
    ]
    improvement_areas = models.ManyToManyField('ImprovementArea')
    comments = models.TextField()

    def __str__(self):
        return self.name


class ImprovementArea(models.Model):
    area = models.CharField(max_length=100)

    def __str__(self):
        return self.area
