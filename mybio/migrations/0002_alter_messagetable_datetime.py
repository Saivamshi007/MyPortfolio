# Generated by Django 4.2 on 2023-04-20 04:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagetable',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 4, 51, 38, 711298, tzinfo=datetime.timezone.utc)),
        ),
    ]