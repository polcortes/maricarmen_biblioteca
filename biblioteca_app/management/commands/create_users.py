# en biblioteca_app/management/commands/create_users.py

from django.core.management.base import BaseCommand
from faker import Faker
from biblioteca_app.models import Usuari

fake = Faker(['es_ES', 'es_MX'])

class Command(BaseCommand):
    help = 'Crea usuarios de ejemplo'

    def handle(self, *args, **options):
        # Generar usuarios regulares
        for _ in range(35):
            nom = fake.first_name()
            cognoms = fake.last_name()
            email = f'{nom[0].lower()}{cognoms.lower()}@gmail.com'  # Generar correo electrónico
            password = fake.password()  # Generar una contraseña
            print(f'Correo electrónico: {email}, Contraseña sin encriptar: {password}')  # Imprimir correo electrónico y contraseña sin encriptar
            user = Usuari(
                nom=nom,
                cognoms=cognoms,
                username=f'{nom}_{cognoms}',
                any_naixement=fake.date(),
                email=email,
                tipus='Alumne',
                is_staff=False,
                is_superuser=False,
            )
            user.set_password(password)  # Encriptar y establecer la contraseña
            user.save()

        # Generar usuarios administradores
        for _ in range(5):
            nom = fake.first_name()
            cognoms = fake.last_name()
            email = f'{nom[0].lower()}{cognoms.lower()}@gmail.com'  # Generar correo electrónico
            password = fake.password()  # Generar una contraseña
            print(f'Correo electrónico: {email}, Contraseña sin encriptar: {password}')  # Imprimir correo electrónico y contraseña sin encriptar
            user = Usuari(
                nom=nom,
                cognoms=cognoms,
                username=f'{nom}_{cognoms}',
                any_naixement=fake.date(),
                email=email,
                tipus='Admin',
                is_staff=True,
                is_superuser=False,
            )
            user.set_password(password)  # Encriptar y establecer la contraseña
            user.save()

        # Generar superusuarios
        for _ in range(2):
            nom = fake.first_name()
            cognoms = fake.last_name()
            email = f'{nom[0].lower()}{cognoms.lower()}@gmail.com'  # Generar correo electrónico
            password = fake.password()  # Generar una contraseña
            print(f'Correo electrónico: {email}, Contraseña sin encriptar: {password}')  # Imprimir correo electrónico y contraseña sin encriptar
            user = Usuari(
                nom=nom,
                cognoms=cognoms,
                username=f'{nom}_{cognoms}',
                any_naixement=fake.date(),
                email=email,
                tipus='Super Usuari',
                is_staff=True,
                is_superuser=True,
            )
            user.set_password(password)  # Encriptar y establecer la contraseña
            user.save()

        self.stdout.write(self.style.SUCCESS('Usuarios creados exitosamente'))
