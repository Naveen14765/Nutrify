# Generated by Django 3.2 on 2022-09-20 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrifying', '0014_delete_earnedcalories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitypeople',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
