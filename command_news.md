python -m venv venv

venv\scripts\activate

pip install django

django-admin startproject NewsPaper

cd NewsPaper

python manage.py startapp news

python manage.py startapp accounts

python manage.py makemigrations
python manage.py migrate

python manage.py shell

cd NewsPaper
`from news.models import *`
===================================
python manage.py createsuperuser

python manage.py runserver
