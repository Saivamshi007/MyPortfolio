#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb
gunicorn -w 1 portfolio.wsgi:application
