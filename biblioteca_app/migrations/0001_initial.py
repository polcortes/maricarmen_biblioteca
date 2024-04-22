# Generated by Django 5.0.4 on 2024-04-22 15:53

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCataleg',
            fields=[
                ('id_cataleg', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('titol', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('descripcio', models.TextField()),
                ('lloc_edicio', models.CharField(max_length=100)),
                ('any', models.IntegerField()),
                ('pais', models.CharField(max_length=100)),
                ('signatura', models.CharField(max_length=100)),
                ('exemplars', models.IntegerField()),
                ('url', models.URLField()),
                ('imatge', models.ImageField(upload_to='')),
                ('mides', models.CharField(max_length=100)),
                ('procedencia', models.CharField(max_length=100)),
                ('caracteristiques', models.TextField()),
                ('altra_informacio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_superuser', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('nom', models.CharField(max_length=100)),
                ('cognoms', models.CharField(max_length=100)),
                ('any_naixement', models.DateField()),
                ('correu_ieti', models.EmailField(max_length=254, unique=True)),
                ('tipus', models.CharField(choices=[('alumne', 'Alumne'), ('professor', 'Professor'), ('admin', 'Admin'), ('super-usuari', 'Super Usuari')], max_length=20)),
                ('password', models.CharField(max_length=128)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='BR',
            fields=[
                ('itemcataleg_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biblioteca_app.itemcataleg')),
                ('discografia', models.CharField(max_length=100)),
                ('estil', models.CharField(max_length=100)),
                ('duracio', models.TimeField()),
            ],
            bases=('biblioteca_app.itemcataleg',),
        ),
        migrations.CreateModel(
            name='CD',
            fields=[
                ('itemcataleg_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biblioteca_app.itemcataleg')),
                ('discografia', models.CharField(max_length=100)),
                ('estil', models.CharField(max_length=100)),
                ('duracio', models.TimeField()),
            ],
            bases=('biblioteca_app.itemcataleg',),
        ),
        migrations.CreateModel(
            name='Dispositiu',
            fields=[
                ('itemcataleg_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biblioteca_app.itemcataleg')),
                ('marca', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('capacitat', models.CharField(max_length=100)),
                ('bateria', models.CharField(max_length=100)),
            ],
            bases=('biblioteca_app.itemcataleg',),
        ),
        migrations.CreateModel(
            name='DVD',
            fields=[
                ('itemcataleg_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biblioteca_app.itemcataleg')),
                ('discografia', models.CharField(max_length=100)),
                ('estil', models.CharField(max_length=100)),
                ('duracio', models.TimeField()),
            ],
            bases=('biblioteca_app.itemcataleg',),
        ),
        migrations.CreateModel(
            name='Llibre',
            fields=[
                ('itemcataleg_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biblioteca_app.itemcataleg')),
                ('CDU', models.CharField(max_length=100)),
                ('ISBN', models.IntegerField()),
                ('editorial', models.CharField(max_length=100)),
                ('collecio', models.CharField(max_length=100)),
                ('pagines', models.IntegerField()),
                ('descriptors', models.CharField(blank=True, max_length=100)),
                ('resum', models.TextField()),
                ('volums', models.IntegerField()),
            ],
            bases=('biblioteca_app.itemcataleg',),
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipus', models.CharField(choices=[('info', 'INFO'), ('warning', 'WARNING'), ('error', 'ERROR'), ('fatal', 'FATAL')], max_length=100)),
                ('titol', models.CharField(max_length=100)),
                ('descripcio', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('pathname', models.CharField(max_length=100)),
                ('usuari', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Peticions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('is_accepted', models.BooleanField(default=False)),
                ('usuari', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prestecs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_prestec', models.DateTimeField()),
                ('data_retorn', models.DateTimeField()),
                ('data_limit', models.DateTimeField()),
                ('item_cataleg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca_app.itemcataleg')),
                ('usuari', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reserves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_reserva', models.DateTimeField()),
                ('item_cataleg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca_app.itemcataleg')),
                ('usuari', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
