# Generated by Django 3.2 on 2022-09-18 09:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nutrifying', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitypeople',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
