# Generated by Django 3.2.7 on 2023-05-04 06:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.TextField(max_length=100)),
                ('project_abstract', models.TextField(max_length=800)),
                ('project_tech', models.TextField(max_length=60)),
                ('project_programming_background', models.TextField(max_length=60)),
                ('project_link', models.TextField(max_length=100)),
                ('project_img', models.ImageField(default='./static/img/logo1.JPG', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='TableforMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=20000)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2023, 5, 4, 6, 16, 1, 969764, tzinfo=utc))),
            ],
        ),
    ]
