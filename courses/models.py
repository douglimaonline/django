from django.db import models

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
class Course(Base):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title
    
class Grade(Base):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='grades')
    name = models.CharField(max_length=255)
    feedback = models.TextField(blank=True, default="")
    score = models.DecimalField(max_digits=2, decimal_places=2)
    email = models.EmailField()

    class Meta:
        verbose_name = "Grade"
        verbose_name_plural = "Grades"
        unique_together = ('course', 'email')

    def __str__(self):
        return f"{self.name} - {self.course.title}: {self.score}"