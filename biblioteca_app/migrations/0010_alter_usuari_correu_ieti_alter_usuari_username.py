# Generated by Django 5.0.4 on 2024-04-21 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca_app', '0009_alter_usuari_tipus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuari',
            name='correu_ieti',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='usuari',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
