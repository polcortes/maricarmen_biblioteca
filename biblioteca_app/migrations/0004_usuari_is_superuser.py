# Generated by Django 5.0.4 on 2024-04-21 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca_app', '0003_alter_llibre_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuari',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]