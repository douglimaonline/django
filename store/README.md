## Basic Django Commands

Run these commands in a terminal. Replace `myproject` and `myapp` with your project and app names.

```bash
# Create a Django project and enter its directory
django-admin startproject myproject
cd myproject

# Create an application
python manage.py startapp myapp

# Create and apply database migrations
python manage.py makemigrations
python manage.py migrate

# Start the development server
python manage.py runserver

# Create an administrator account
python manage.py createsuperuser

# Run tests
python manage.py test
```
