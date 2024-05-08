# en biblioteca_app/management/commands/create_users.py

from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password

from faker import Faker
from biblioteca_app.models import Usuari
from datetime import datetime, timedelta

fake = Faker(['es_ES', 'es_MX'])

class Command(BaseCommand):
    help = 'Crea usuarios de ejemplo'

    def handle(self, *args, **options):
        # Generar usuarios regulares
        for _ in range(35):
            nom = fake.first_name()
            cognoms = fake.last_name()
            
            usuari = Usuari(
                nom = nom,
                cognoms = cognoms,
                username = f'{nom}_{cognoms}',
                any_naixement = fake.date_between_dates(date_start=datetime(1969,1,1), date_end=datetime(2011,12,31)),
                email = f'{nom[0].lower()}{cognoms.lower()}@gmail.com',
                tipus = 'usuari',
                centre = f'I.E.S. Esteve Terradas i Illa',
                password = make_password('12345678aA@'),
                is_staff = False,
                is_superuser = False,
            )
            usuari.save()

        for _ in range(5):
            nom = fake.first_name()
            cognoms = fake.last_name()

            usuari = Usuari(
                nom = nom,
                cognoms = cognoms,
                username = f'{nom}_{cognoms}',
                any_naixement = fake.date_between_dates(date_start=datetime(1969,1,1), date_end=datetime(2011,12,31)),
                email = f'{nom[0].lower()}{cognoms.lower()}@gmail.com',
                tipus = 'admin',
                centre = f'I.E.S. Esteve Terradas i Illa',
                password = make_password('12345678aA@'),
                is_staff = True,
                is_superuser = False,
            )
            usuari.save()

        for _ in range(2):
            nom = fake.first_name()
            cognoms = fake.last_name()

            usuari = Usuari(
                nom = nom,
                cognoms = cognoms,
                username = f'{nom}_{cognoms}',
                any_naixement = fake.date_between_dates(date_start=datetime(1969,1,1), date_end=datetime(2011,12,31)),
                email = f'{nom[0].lower()}{cognoms.lower()}@gmail.com',
                tipus = 'super-usuari',
                centre = f'I.E.S. Esteve Terradas i Illa',
                password = make_password('12345678aA@'),
                is_staff = True,
                is_superuser = True,
            )
            usuari.save()

        self.stdout.write(self.style.SUCCESS('Usuarios creados exitosamente'))
