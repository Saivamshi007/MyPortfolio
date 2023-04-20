#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py migrate
gunicorn -w 1 portfolio.wsgi:application
