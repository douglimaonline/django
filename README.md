# Django basics

This repository is a Django project named `ecommerce`. It uses SQLite for its
database and lists Django in `requirements.txt`.

## Set up the project

Run these commands from the project root:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install the project dependencies:

```bash
python -m pip install -r requirements.txt
```

## Common Django commands

Run the development server:

```bash
python manage.py runserver
```

By default, open <http://127.0.0.1:8000/> in a browser. The development server
is intended for local development, not production.

Create database migration files after changing models, then apply them:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create an administrator account and open the Django admin at
<http://127.0.0.1:8000/admin/>:

```bash
python manage.py createsuperuser
```

Run the project’s tests:

```bash
python manage.py test
```

Open Django’s interactive Python shell:

```bash
python manage.py shell
```

Check the project for common configuration problems:

```bash
python manage.py check
```

See which migrations are applied:

```bash
python manage.py showmigrations
```

## Creating an app

Create an app inside the project:

```bash
python manage.py startapp <app_name>
```

After creating it, add the app to `INSTALLED_APPS` in
`ecommerce/settings.py`. Define its models, create migrations with
`makemigrations`, and apply them with `migrate`.

Replace `<app_name>` with the app's Python package name. Run `manage.py`
commands from the directory containing `manage.py`.
