# Generated by Django 3.2 on 2022-09-19 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrifying', '0004_alter_datefield_userinput'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datefield',
            name='userinput',
            field=models.DateField(),
        ),
    ]
