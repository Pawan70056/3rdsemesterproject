from django.contrib import admin
from django.utils.html import format_html

from .models import (Book, Chapter, ContactMessage, Content, Course,
                     CourseCategory, Feedback, ImprovementArea, MyCourses,
                     Ticket)


# Define a mixin class to display thumbnails
class ThumbnailDisplayMixin:
    def display_thumbnail(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.thumbnail.url if obj.thumbnail else '')

    display_thumbnail.short_description = 'Thumbnail'
    display_thumbnail.allow_tags = True


class DescriptionDisplayMixin:
    def display_short_description(self, obj):
        if len(obj.description) > 200:
            return f"{obj.description[:200]}..."
        return obj.description

    display_short_description.short_description = 'Short Description'


# Register CourseCategory model
@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin, ThumbnailDisplayMixin,DescriptionDisplayMixin ):
    list_display = ('display_thumbnail', 'name', 'display_short_description')

# Register Course model
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin, ThumbnailDisplayMixin, DescriptionDisplayMixin):
    list_display = ('display_thumbnail', 'title', 'display_short_description', 'instructor', 'category', 'created_at', 'updated_at')
    list_filter = ('category', 'instructor', 'created_at', 'updated_at')
    search_fields = ('title', 'description')

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    list_filter = ('course',)
    search_fields = ('title',)

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('chapter','content_type' )
    list_filter = ('chapter__course', 'content_type')
    search_fields = ('chapter__title',)



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'category') 
    list_filter = ('author', 'published_date', 'category') 
    search_fields = ('title', 'author__name')  
    

@admin.register(MyCourses)
class MyCoursesAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'date_enrolled')
    list_filter = ( 'course',)
    search_fields = ('user__username', 'course__title',)
  
    
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age', 'employment_status', 'experience_level', 'course_rating')
    list_filter = ('employment_status', 'experience_level', 'course_rating')
    search_fields = ('name', 'email')

     # Disable add, update, and delete actions
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ImprovementArea)
class ImprovementAreaAdmin(admin.ModelAdmin):
    list_display = ('area',)
    search_fields = ('area',)

     # Disable add, update, and delete actions
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'feedback_type', 'severity', 'message')
    search_fields = ('name', 'email', 'feedback_type', 'severity', 'message')

      # Disable add, update, and delete actions
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email', 'message')
    list_filter = ('name', 'email')

    
