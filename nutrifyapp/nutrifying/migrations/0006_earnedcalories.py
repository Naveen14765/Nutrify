# Generated by Django 3.2 on 2022-09-19 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrifying', '0005_alter_datefield_userinput'),
    ]

    operations = [
        migrations.CreateModel(
            name='EarnedCalories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories_remained', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
