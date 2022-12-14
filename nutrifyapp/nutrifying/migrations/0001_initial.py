# Generated by Django 3.2 on 2022-09-18 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityPeople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posts', models.ImageField(null=True, upload_to='images')),
                ('comment', models.TextField(null=True)),
                ('userName', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DateField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userinput', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Excercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excercise', models.CharField(max_length=50)),
                ('calories', models.IntegerField(blank=True, null=True)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('userName', models.CharField(max_length=50, null=True)),
                ('currentdate', models.DateField(default=datetime.date(2022, 9, 18))),
            ],
        ),
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.CharField(max_length=50)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('calories', models.IntegerField(blank=True, null=True)),
                ('userName', models.CharField(max_length=50, null=True)),
                ('currentdate', models.DateField(default=datetime.date(2022, 9, 18))),
            ],
        ),
    ]
