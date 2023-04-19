# Generated by Django 3.2.7 on 2023-04-13 10:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mybio', '0005_auto_20230413_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagetable',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 13, 10, 8, 43, 888551, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projecttable',
            name='project_abstract',
            field=models.TextField(max_length=400),
        ),
    ]