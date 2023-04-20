@ECHO ON
    call python manage.py makemigrations
    call python manage.py migrate
    call gunicorn -w 1 portfolio.wsgi:application
