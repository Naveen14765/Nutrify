# Generated by Django 3.2 on 2022-09-19 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrifying', '0007_earnedcalories_time_maintained'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitypeople',
            name='timestamp',
            field=models.DateTimeField(default=datetime.date(2022, 9, 20)),
        ),
        migrations.AlterField(
            model_name='excercise',
            name='currentdate',
            field=models.DateField(default=datetime.date(2022, 9, 20)),
        ),
        migrations.AlterField(
            model_name='health',
            name='currentdate',
            field=models.DateField(default=datetime.date(2022, 9, 20)),
        ),
    ]