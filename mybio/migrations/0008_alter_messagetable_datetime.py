# Generated by Django 3.2.7 on 2023-04-13 12:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mybio', '0007_auto_20230413_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagetable',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 13, 12, 19, 3, 142174, tzinfo=utc)),
        ),
    ]
