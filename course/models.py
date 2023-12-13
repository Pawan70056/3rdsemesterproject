from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
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
