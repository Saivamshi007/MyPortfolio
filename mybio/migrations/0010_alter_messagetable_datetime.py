# Generated by Django 3.2.7 on 2023-04-14 05:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mybio', '0009_alter_messagetable_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagetable',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 14, 5, 29, 31, 831625, tzinfo=utc)),
        ),
    ]