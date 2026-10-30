from django.urls import path

from .views import CourseAPIView, GradeAPIView

urlpatterns = [
    path('courses/', CourseAPIView.as_view(), name='courses'),
    path('grades/', GradeAPIView.as_view(), name='grades'),
]
