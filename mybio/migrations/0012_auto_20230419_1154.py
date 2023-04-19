# Generated by Django 3.2.7 on 2023-04-19 06:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mybio', '0011_auto_20230418_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecttable',
            name='project_img',
            field=models.ImageField(default='./static/img/logo1.JPG', upload_to=''),
        ),
        migrations.AlterField(
            model_name='messagetable',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 19, 6, 24, 35, 264311, tzinfo=utc)),
        ),
    ]
