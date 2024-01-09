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

