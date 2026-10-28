from django.contrib import admin
from .models import Course, Grade

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'created_at', 'updated_at')
    search_fields = ('title', 'url')
    ordering = ('-created_at',)
    
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'score', 'email', 'created_at', 'updated_at')
    search_fields = ('name', 'course__title', 'email')
    ordering = ('-created_at',)
    list_filter = ('course',)