from rest_framework import serializers

from .models import Course, Grade

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'url', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('id', 'course', 'student', 'grade', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')