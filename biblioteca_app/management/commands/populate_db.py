from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from random import randint, choice
from biblioteca_app.models import *

from faker import Faker
from datetime import datetime, timedelta

fake = Faker(['es_ES'])

class Command(BaseCommand):
    help = 'Genera dades fictícies per a la base de dades'
    def handle(self, *args, **options):
        autores = []
        caracteristiques_llibres = ['Edició de butxaca', 'Edició de luxe', 'Edició de tapa dura', 'Edició de tapa tova']

        # Generar llibres
        for _ in range(100):
            nouAutor = fake.name()
            while nouAutor in autores:
                nouAutor = fake.name()
            autores.append(nouAutor)

        centres = []

        for _ in range(30):
            centre = f'INS {fake.first_name()} {fake.last_name()}'
            while centre in centres:
                centre = f'INS {fake.first_name()} {fake.last_name()}'
            centres.append(centre)

        articulos = ['el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas']
        nombres_comunes = ['perro', 'gato', 'mesa', 'silla', 'coche', 'casa', 'pueblo', 'ciudad', 'país', 'continente', 'planeta', 'universo', 'lápiz', 'bolígrafo', 'libreta', 'cuaderno', 'papel', 'cartón', 'plástico', 'metal', 'madera', 'vidrio', 'cerámica', 'piedra', 'arena', 'tierra', 'agua', 'aire', 'fuego', 'hierro', 'cobre', 'aluminio', 'plata', 'oro', 'diamante', 'esmeralda', 'rubí', 'zafiro', 'topacio', 'cuarzo', 'granito', 'mármol', 'caliza', 'arcilla', 'barro', 'yeso', 'cemento', 'asfalto', 'piedra pómez', 'piedra volcánica', 'piedra caliza', 'piedra arenisca', 'piedra basáltica', 'piedra de río', 'piedra de cantera', 'piedra de mármol', 'piedra de granito', 'piedra de cuarzo', 'piedra de ónix', 'piedra de jade', 'piedra de ámbar', 'piedra de coral', 'piedra de luna', 'piedra de sol', 'piedra de estrella', 'piedra de cometa', 'piedra de meteorito', 'piedra de asteroide', 'piedra de planeta', 'piedra de galaxia', 'piedra de universo', 'piedra de multiverso', 'piedra de omniverso', 'piedra de hiperverso', 'piedra de ultraverso', 'piedra de megaverso', 'piedra de gigaverso', 'piedra de teraverso', 'piedra de exaverso', 'piedra de zettaverso', 'piedra de yottaverso', 'piedra de xennaverso', 'piedra de wekaverso', 'piedra de vundaverso', 'piedra de uundaverso', 'piedra de tundaverso', 'piedra de sundaverso', 'piedra de rundaverso', 'piedra de qundaverso', 'piedra de pundaverso', 'piedra de oundaverso', 'piedra de nundaverso', 'piedra de mundaverso', 'piedra de lundaverso', 'piedra de kundaverso', 'piedra de jundaverso', 'piedra de iundaverso', 'piedra de hundaverso', 'piedra de gundaverso', 'piedra de fundaverso', 'piedra de eundaverso', 'piedra de dundaverso', 'piedra de cundaverso', 'piedra de bundaverso', 'piedra de aundaverso']
        adjetivos = ['rojo', 'azul', 'verde', 'amarillo', 'naranja', 'violeta', 'morado', 'rosa', 'blanco', 'guapo', 'feo', 'alto', 'bajo', 'gordo', 'flaco', 'fuerte', 'débil', 'inteligente', 'tonto', 'listo', 'listillo']

        for autor in autores:
            for _ in range(randint(1, 10)):
                llibre = Llibre(
                    titol=f'{choice(articulos)} {choice(nombres_comunes)} {choice(adjetivos)}',
                    autor=autor,
                    descripcio=fake.text(),
                    lloc_edicio=fake.city(),
                    any=fake.year(),
                    pais=fake.country(),
                    signatura=fake.ean8(),
                    exemplars=randint(0, 10),
                    url=fake.url(),
                    imatge=fake.image_url(),
                    mides="10x15",
                    procedencia=fake.company(),
                    llengua=choice(['Català', 'Castellà', 'Anglès', 'Francès', 'Alemany', 'Italià', 'Portuguès', 'Àrab', 'Grec', 'Hebreu', 'Llatí']),
                    centre=choice(centres),
                    caracteristiques=choice(caracteristiques_llibres),
                    altra_informacio=fake.text(),
                    CDU=fake.ean8(),
                    editorial=fake.company(),
                    ISBN = int(fake.isbn10().replace('-', '').replace('X', '')), 
                    colleccio = fake.word(),
                    pagines = randint(50, 1100),
                    descriptors = fake.words(),
                    resum = fake.text(),
                    volums = randint(1, 13),
                    tipus = 'llibre',
                )
                llibre.save()

        procedencies_dvds = ['Versió remasteritzada', 'Versió en directe']
        estils_dvds = ['Rock', 'Pop', 'Jazz', 'Clàssica', 'Electrònica', 'Hip-Hop', 'Reggae', 'Metal', 'Punk', 'Country', 'Blues', 'Folk', 'Rap', 'Soul', 'R&B', 'Indie', 'Alternativa', 'Dance', 'House', 'Techno', 'Ambient', 'Dubstep', 'Trap', 'Reggaeton', 'Ska', 'Gospel', 'Funk', 'Disco', 'New Age', 'Flamenc', 'Celta', 'Ska', 'Salsa', 'Bachata', 'Merengue', 'Tango', 'Ranchera', 'Mariachi', 'Bolero', 'Samba', 'Bossa Nova', 'Forró', 'Fado', 'Morna', 'Música clàssica', 'Música contemporània', 'Música experimental', 'Música minimalista', 'Música concreta', 'Música aleatòria', 'Música electroacústica', 'Música dodecafònica', 'Música serial', 'Música microtonal', 'Música concreta', 'Música aleatòria', 'Música electroacústica', 'Música dodecafònica', 'Música serial', 'Música microtonal', 'Música concreta', 'Música aleatòria', 'Música electroacústica', 'Música dodecafònica', 'Música serial', 'Música microtonal', 'Música concreta', 'Música aleatòria', 'Música electroacústica', 'Música dodecafònica', 'Música serial', 'Música microtonal', 'Música concreta', 'Música aleatòria', 'Música electroacústica', 'Música dodecafònica', 'Música serial', 'Música microtonal', 'Música concreta', 'Música aleatòria', 'Música electroacústica', 'Música dodecafònica']

        # Generar DVDs
        for _ in range(35):
            dvd = DVD(
                titol = f'{choice(articulos)} {choice(nombres_comunes)} {choice(adjetivos)}',
                autor = fake.name(),
                descripcio = fake.text(),
                lloc_edicio = fake.city(),
                any = fake.year(),
                pais = fake.country(),
                signatura = fake.ean8(),
                exemplars = randint(0, 10),
                url = fake.url(),
                imatge = fake.image_url(),
                mides = "10x15",
                procedencia = fake.company(),
                llengua=choice(['Català', 'Castellà', 'Anglès', 'Francès', 'Alemany', 'Italià', 'Portuguès', 'Àrab', 'Grec', 'Hebreu', 'Llatí']),
                centre=choice(centres),
                caracteristiques = choice(procedencies_dvds),
                altra_informacio = fake.text(),
                discografia = fake.company(),
                estil = choice(estils_dvds),
                duracio = f'0{randint(0, 1)}:{randint(0,59)}:{randint(0,59)}',
                tipus = 'dvd',
            )
            dvd.save()

        procedencies_cds = ['Versió remasteritzada', 'Versió en directe']
        estils_cds = ['Rock', 'Pop', 'Jazz', 'Clàssica', 'Electrònica', 'Hip-Hop', 'Reggae', 'Metal', 'Punk', 'Country', 'Blues', 'Folk', 'Rap', 'Soul', 'R&B', 'Indie', 'Alternativa', 'Dance', 'House', 'Techno', 'Ambient', 'Dubstep', 'Trap', 'Reggaeton', 'Ska', 'Gospel', 'Funk', 'Disco', 'New Age', 'Flamenc', 'Celta', 'Ska', 'Salsa', 'Bachata', 'Merengue', 'Tango', 'Ranchera', 'Mariachi', 'Bolero', 'Samba', 'Bossa Nova', 'Forró', 'Fado', 'Morna', 'Música clàssica', 'Música contemporània', 'Música experimental', 'Música minimalista', 'Música concreta', 'Música aleatòria', 'Música electroacústica', 'Música dodecafònica', 'Música serial', 'Música microtonal', 'Música concreta', 'Música aleatòria', 'Música electroacústica', 'Música dodecafònica', 'Música serial', 'Música microtonal', 'Música concreta', 'Música aleatòria', 'Música electroacústica', 'Música dodecafònica', 'Música serial', 'Música microtonal', 'Música concreta', 'Música aleatòria', 'Música electroacústica', 'Música dodecafònica', 'Música serial', 'Música microtonal', 'Música concreta', 'Música aleatòria', 'Música electroacústica', 'Música dodecafònica', 'Música serial', 'Música microtonal', 'Música concreta', 'Música aleatòria', 'Música electroacústica', 'Música dodecafònica']

        # Generar CDs
        for _ in range(35):
            cd = CD(
                titol = f'{choice(articulos)} {choice(nombres_comunes)} {choice(adjetivos)}',
                autor = fake.name(),
                descripcio = fake.text(),
                lloc_edicio = fake.city(),
                any = fake.year(),
                pais = fake.country(),
                signatura = fake.ean8(),
                exemplars = randint(0, 10),
                url = fake.url(),
                imatge = fake.image_url(),
                mides = "10x15",
                procedencia = fake.company(),
                llengua=choice(['Català', 'Castellà', 'Anglès', 'Francès', 'Alemany', 'Italià', 'Portuguès', 'Àrab', 'Grec', 'Hebreu', 'Llatí']),
                centre=choice(centres),
                caracteristiques = choice(procedencies_cds),
                altra_informacio = fake.text(),
                discografia = fake.company(),
                estil = choice(estils_cds),
                duracio = f'0{randint(0, 1)}:{randint(0,59)}:{randint(0,59)}',
                tipus = 'cd',
            )
            cd.save()


        procedencies_brs = ['Versió remasteritzada', 'Versió en directe']
        estils_brs = ['Rock', 'Pop', 'Jazz', 'Clàssica', 'Electrònica', 'Hip-Hop', 'Reggae', 'Metal', 'Punk', 'Country', 'Blues', 'Folk', 'Rap', 'Soul', 'R&B', 'Indie', 'Alternativa', 'Dance', 'House', 'Techno', 'Ambient', 'Dubstep', 'Trap', 'Reggaeton', 'Ska', 'Gospel', 'Funk', 'Disco', 'New Age', 'Flamenc', 'Celta', 'Ska', 'Salsa', 'Bachata', 'Merengue', 'Tango', 'Ranchera', 'Mariachi', 'Bolero', 'Samba', 'Bossa Nova', 'Forró', 'Fado', 'Morna', 'Música clàssica', 'Música contemporània', 'Música experimental', 'Música minimalista', 'Música concreta', 'Música aleatòria', 'Música electroacústica', 'Música dodecafònica', 'Música serial', 'Música microtonal', 'Música concreta', 'Música aleatòria', 'Música electroacústica', 'Música dodecafònica', 'Música serial', 'Música microtonal', 'Música concreta', 'Música aleatòria', 'Música electroacústica', 'Música dodecafònica', 'Música serial', 'Música microtonal', 'Música concreta', 'Música aleatòria', 'Música electroacústica', 'Música dodecafònica', 'Música serial', 'Música microtonal', 'Música concreta', 'Música aleatòria', 'Música electroacústica', 'Música dodecafònica', 'Música serial', 'Música microtonal', 'Música concreta', 'Música aleatòria', 'Música electroacústica', 'Música dodecafònica']

        # Generar BRs
        for _ in range(35):
            br = BR(
                titol = f'{choice(articulos)} {choice(nombres_comunes)} {choice(adjetivos)}',
                autor = fake.name(),
                descripcio = fake.text(),
                lloc_edicio = fake.city(),
                any = fake.year(),
                pais = fake.country(),
                signatura = fake.ean8(),
                exemplars = randint(0, 10),
                url = fake.url(),
                imatge = fake.image_url(),
                mides = "10x15",
                procedencia = fake.company(),
                llengua=choice(['Català', 'Castellà', 'Anglès', 'Francès', 'Alemany', 'Italià', 'Portuguès', 'Àrab', 'Grec', 'Hebreu', 'Llatí']),
                centre=choice(centres),
                caracteristiques = choice(procedencies_brs),
                altra_informacio = fake.text(),
                discografia = fake.company(),
                estil = choice(estils_brs),
                duracio = f'0{randint(0, 1)}:{randint(0,59)}:{randint(0,59)}',
                tipus = 'br',
            )
            br.save()

        # Generar dispositius
        for _ in range(35):
            dispositiu = Dispositiu(
                titol = f'EBook {choice(["rojo", "azul", "verde", "negro", "blanco"])}',
                autor = fake.name(),
                descripcio = fake.text(),
                lloc_edicio = fake.city(),
                any = fake.year(),
                pais = fake.country(),
                signatura = fake.ean8(),
                exemplars = randint(0, 10),
                url = fake.url(),
                imatge = fake.image_url(),
                mides = "10x15",
                procedencia = fake.company(),
                llengua=choice(['Català', 'Castellà', 'Anglès', 'Francès', 'Alemany', 'Italià', 'Portuguès', 'Àrab', 'Grec', 'Hebreu', 'Llatí']),
                centre=choice(centres),
                caracteristiques = choice(procedencies_brs),
                altra_informacio = fake.text(),
                marca = fake.company(),
                model = fake.word(),
                capacitat = choice(['8GB', '16GB', '32GB', '64GB', '128GB', '256GB', '512GB', '1TB']),
                bateria = choice(['1000mAh', '2000mAh', '3000mAh', '4000mAh', '5000mAh', '6000mAh', '7000mAh', '8000mAh', '9000mAh', '10000mAh']),
                tipus = 'dispositiu',
            )
            dispositiu.save()

        usuaris = []

        # Generar usuaris:
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
                centre = f'INS {fake.first_name()} {fake.last_name()}',
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
                centre = f'INS {fake.first_name()} {fake.last_name()}',
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
                centre = f'INS {fake.first_name()} {fake.last_name()}',
                password = make_password('12345678aA@'),
                is_staff = True,
                is_superuser = True,
            )
            usuari.save()

        # Generar reserves
        for usuari in Usuari.objects.all():
            timesdone = 0
            while timesdone < 3:
                if (randint(0,1) == 1):
                    data_reserva = datetime.now() - timedelta(days=randint(1, 365))
                    data_limit = data_reserva + timedelta(days=randint(1, 30))

                    reserva = Reserves(
                        usuari = usuari,
                        item_cataleg = ItemCataleg.objects.all().order_by('?').first(),
                        data_reserva = data_reserva,
                    )
                    reserva.save()
                    timesdone += 1

        # Generar prestecs
        for usuari in Usuari.objects.all():
            timesdone = 0
            while timesdone < 3:
                if (randint(0,1) == 1):
                    data_prestec = datetime.now() - timedelta(days=randint(1, 365))
                    data_retorn = choice([data_prestec + timedelta(days=randint(1, 30)), None])
                    data_limit = data_prestec + timedelta(days=30)

                    prestec = Prestecs(
                        usuari = usuari,
                        item_cataleg = ItemCataleg.objects.all().order_by('?').first(),
                        data_prestec = data_prestec,
                        data_retorn = data_retorn,
                        data_limit = data_prestec + timedelta(days=30)
                    )
                    prestec.save()
                    timesdone += 1

        # Generar peticions
        for usuari in Usuari.objects.all():
            timesdone = 0
            while timesdone < 3:
                if (randint(0,1) == 1):
                    peticio = Peticions(
                        usuari = usuari,
                        text = fake.text(),
                        is_accepted = False,
                    )
                    peticio.save()
                    timesdone += 1

        for usuari in usuaris:
            self.stdout.write(f"{usuari['correo']} -> {usuari['contraseña']}")

        self.stdout.write(self.style.SUCCESS('Dades creades correctament.'))