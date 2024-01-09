from django.contrib import admin
from django.utils.html import format_html

from .models import Book, Chapter, Content, Course, CourseCategory, MyCourses


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
