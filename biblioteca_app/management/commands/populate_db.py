import random
from django.contrib.auth import get_user_model
from django.utils import timezone
from biblioteca_app.models import *

def create_users():
    User = get_user_model()
    users = [
        {'nom': 'John', 'cognoms': 'Doe', 'any_naixement': '1990-05-15', 'correu_ieti': 'john.doe@iesesteveterradas.cat', 'tipus': 'alumne'},
        {'nom': 'Jane', 'cognoms': 'Smith', 'any_naixement': '1985-03-20', 'correu_ieti': 'jane.smith@iesesteveterradas.cat', 'tipus': 'professor'},
        {'nom': 'Admin', 'cognoms': 'Admin', 'any_naixement': '1980-10-10', 'correu_ieti': 'admin@iesesteveterradas.cat', 'tipus': 'admin'},
    ]
    for user_data in users:
        User.objects.create_user(email=user_data['correu_ieti'], password='password123', **user_data)

def create_items():
    items = [
        {'titol': 'El gran Gatsby', 'autor': 'F. Scott Fitzgerald', 'descripcio': 'Novela clásica que retrata la vida en la alta sociedad estadounidense durante la década de 1920.', 'lloc_edicio': 'Nueva York', 'any': 1925, 'pais': 'Estados Unidos', 'signatura': 'FIC-001', 'exemplars': 5, 'url': 'https://example.com', 'imatge': 'gatsby.jpg', 'mides': '14x21', 'procedencia': 'Donación biblioteca', 'caracteristiques': 'Edición de tapa dura', 'altra_informacio': 'Incluye notas al pie de página'},
        {'titol': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'descripcio': 'Obra maestra del realismo mágico latinoamericano que narra la historia de la familia Buendía en el pueblo ficticio de Macondo.', 'lloc_edicio': 'Bogotá', 'any': 1967, 'pais': 'Colombia', 'signatura': 'FIC-002', 'exemplars': 3, 'url': 'https://example.com', 'imatge': 'cien_anos_soledad.jpg', 'mides': '15x23', 'procedencia': 'Compra biblioteca', 'caracteristiques': 'Edición de bolsillo', 'altra_informacio': 'Versión revisada por el autor'},
    ]
    for item_data in items:
        ItemCataleg.objects.create(**item_data)

def create_prestecs():
    users = get_user_model().objects.all()
    items = ItemCataleg.objects.all()
    for _ in range(5):
        user = random.choice(users)
        item = random.choice(items)
        Prestecs.objects.create(usuari=user, item_cataleg=item, data_prestec=timezone.now(), data_retorn=timezone.now() + timezone.timedelta(days=14), data_limit=timezone.now() + timezone.timedelta(days=30))

def create_reserves():
    users = get_user_model().objects.all()
    items = ItemCataleg.objects.all()
    for _ in range(3):
        user = random.choice(users)
        item = random.choice(items)
        Reserves.objects.create(usuari=user, item_cataleg=item, data_reserva=timezone.now())

def create_peticions():
    users = get_user_model().objects.all()
    for _ in range(2):
        user = random.choice(users)
        Peticions.objects.create(usuari=user, text='Solicitud de información', is_accepted=False)

def create_books():
    books = [
        {'titol': 'El guardián entre el centeno', 'autor': 'J.D. Salinger', 'descripcio': 'Novela que relata la odisea de Holden Caulfield por las calles de Nueva York.', 'lloc_edicio': 'Nueva York', 'any': 1951, 'pais': 'Estados Unidos', 'signatura': 'FIC-003', 'exemplars': 4, 'url': 'https://example.com', 'imatge': 'guardian_centeno.jpg', 'mides': '12x18', 'procedencia': 'Compra biblioteca', 'caracteristiques': 'Edición de tapa blanda', 'altra_informacio': 'Incluye prólogo del autor'},
        {'titol': 'Moby Dick', 'autor': 'Herman Melville', 'descripcio': 'Novela épica que narra la obsesión del capitán Ahab por cazar a la ballena blanca.', 'lloc_edicio': 'Londres', 'any': 1851, 'pais': 'Reino Unido', 'signatura': 'FIC-004', 'exemplars': 2, 'url': 'https://example.com', 'imatge': 'moby_dick.jpg', 'mides': '16x24', 'procedencia': 'Donación biblioteca', 'caracteristiques': 'Edición de lujo', 'altra_informacio': 'Incluye ilustraciones originales'},
    ]
    for book_data in books:
        Llibre.objects.create(**book_data)

def create_cds():
    cds = [
        {'titol': 'Dark Side of the Moon', 'autor': 'Pink Floyd', 'descripcio': 'Álbum clásico de rock progresivo que explora temas como la vida, la muerte y la locura.', 'lloc_edicio': 'Londres', 'any': 1973, 'pais': 'Reino Unido', 'signatura': 'CD-001', 'exemplars': 3, 'url': 'https://example.com', 'imatge': 'dark_side_moon.jpg', 'mides': '12x12', 'procedencia': 'Compra biblioteca', 'caracteristiques': 'Edición remasterizada', 'altra_informacio': 'Incluye póster'},
        {'titol': 'Thriller', 'autor': 'Michael Jackson', 'descripcio': 'Álbum más vendido de todos los tiempos que revolucionó la industria musical con sus innovadores vídeos musicales.', 'lloc_edicio': 'Los Ángeles', 'any': 1982, 'pais': 'Estados Unidos', 'signatura': 'CD-002', 'exemplars': 5, 'url': 'https://example.com', 'imatge': 'thriller.jpg', 'mides': '14x14', 'procedencia': 'Donación biblioteca', 'caracteristiques': 'Edición especial aniversario', 'altra_informacio': 'Incluye material extra'},
    ]
    for cd_data in cds:
        CD.objects.create(**cd_data)

def create_dvds():
    dvds = [
        {'titol': 'Pulp Fiction', 'autor': 'Quentin Tarantino', 'descripcio': 'Película icónica del cine contemporáneo que entrelaza varias historias sobre crimen y redención en Los Ángeles.', 'lloc_edicio': 'Los Ángeles', 'any': 1994, 'pais': 'Estados Unidos', 'signatura': 'DVD-001', 'exemplars': 3, 'url': 'https://example.com', 'imatge': 'pulp_fiction.jpg', 'mides': '12x12', 'procedencia': 'Compra biblioteca', 'caracteristiques': 'Edición especial coleccionista', 'altra_informacio': 'Incluye escenas eliminadas'},
        {'titol': 'El Señor de los Anillos: La Comunidad del Anillo', 'autor': 'Peter Jackson', 'descripcio': 'Primera entrega de la trilogía épica basada en la obra de J.R.R. Tolkien que sigue el viaje de un joven hobbit para destruir un poderoso anillo.', 'lloc_edicio': 'Nueva Zelanda', 'any': 2001, 'pais': 'Nueva Zelanda', 'signatura': 'DVD-002', 'exemplars': 4, 'url': 'https://example.com', 'imatge': 'senor_anillos.jpg', 'mides': '14x14', 'procedencia': 'Donación biblioteca', 'caracteristiques': 'Edición extendida', 'altra_informacio': 'Incluye documentales del making-of'},
    ]
    for dvd_data in dvds:
        DVD.objects.create(**dvd_data)

def create_brs():
    brs = [
        {'titol': 'Blade Runner', 'autor': 'Ridley Scott', 'descripcio': 'Película de ciencia ficción distópica que sigue al ex-policía Rick Deckard mientras persigue a replicantes rebeldes en un Los Ángeles futurista.', 'lloc_edicio': 'Los Ángeles', 'any': 1982, 'pais': 'Estados Unidos', 'signatura': 'BR-001', 'exemplars': 2, 'url': 'https://example.com', 'imatge': 'blade_runner.jpg', 'mides': '12x12', 'procedencia': 'Compra biblioteca', 'caracteristiques': 'Edición remasterizada en Blu-ray', 'altra_informacio': 'Incluye comentarios del director'},
        {'titol': 'Origen', 'autor': 'Christopher Nolan', 'descripcio': 'Película de ciencia ficción que explora los límites de la realidad y los sueños mientras un grupo de ladrones expertos intenta implantar una idea en la mente de un empresario.', 'lloc_edicio': 'Los Ángeles', 'any': 2010, 'pais': 'Estados Unidos', 'signatura': 'BR-002', 'exemplars': 3, 'url': 'https://example.com', 'imatge': 'inception.jpg', 'mides': '14x14', 'procedencia': 'Donación biblioteca', 'caracteristiques': 'Edición especial de coleccionista', 'altra_informacio': 'Incluye entrevistas con el elenco'},
    ]
    for br_data in brs:
        BR.objects.create(**br_data)

def create_dispositius():
    dispositius = [
        {'marca': 'Apple', 'model': 'iPhone 13', 'capacitat': '128 GB', 'bateria': '3500 mAh'},
        {'marca': 'Samsung', 'model': 'Galaxy S22', 'capacitat': '256 GB', 'bateria': '4000 mAh'},
        {'marca': 'Google', 'model': 'Pixel 6', 'capacitat': '256 GB', 'bateria': '3800 mAh'},
    ]
    for dispositiu_data in dispositius:
        Dispositiu.objects.create(**dispositiu_data)

create_users()
create_items()
create_prestecs()
create_reserves()
create_peticions()
create_books()
create_cds()
create_dvds()
create_brs()
create_dispositius()