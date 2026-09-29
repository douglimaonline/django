from django.shortcuts import render
from .models import User

# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def users(request):
    new_user = User()
    new_user.name = request.POST.get('name')
    new_user.age = request.POST.get('age')
    new_user.save()

    users = User.objects.all()
    return render(request, 'users/users.html', {'users': users})