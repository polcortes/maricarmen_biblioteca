# Generated by Django 5.0.4 on 2024-05-08 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuari',
            name='any_naixement',
            field=models.DateField(default='2000-01-01'),
        ),
    ]
