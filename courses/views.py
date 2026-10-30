from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, Grade
from .serializers import CourseSerializer, GradeSerializer

class CourseAPIView(APIView): # add filter parameters for course title
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GradeAPIView(APIView):
    def get(self, request):
        grades = Grade.objects.all()
        serializer = GradeSerializer(grades, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GradeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, pk):
        try:
            grade = Grade.objects.get(pk=pk)
        except Grade.DoesNotExist:
            return Response({"error": "Grade not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = GradeSerializer(grade, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)