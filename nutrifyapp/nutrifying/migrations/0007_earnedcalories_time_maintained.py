# Generated by Django 3.2 on 2022-09-19 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrifying', '0006_earnedcalories'),
    ]

    operations = [
        migrations.AddField(
            model_name='earnedcalories',
            name='time_maintained',
            field=models.DateTimeField(auto_now=True),
        ),
    ]