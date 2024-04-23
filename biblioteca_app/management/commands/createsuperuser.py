from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.utils.translation import gettext as _
from getpass import getpass
import datetime

class Command(BaseCommand):
    help = 'Crea un superusuario personalizado utilizando el modelo Usuari'

    def handle(self, *args, **options):
        Usuari = get_user_model()
        username_field = Usuari._meta.get_field(Usuari.USERNAME_FIELD)
        database = options.get('database')

        # Solicitar los detalles del superusuario al usuario
        #TODO: Valorar cambiar esto por el username:
        # correu_ieti = None
        # while correu_ieti is None:
        #     input_msg = _('Correu electrònic IETI: ')
        #     correu_ieti = input(input_msg).encode('utf-8')

        #     try:
        #         Usuari._default_manager.db_manager(database).get(**{
        #             username_field.name: correu_ieti
        #         })
        #     except Usuari.DoesNotExist:
        #         break
        #     else:
        #         self.stderr.write("El correu electrònic ja està en ús. Si us plau, introdueix un altre.")

        username = None
        while username is None:
            input_msg = _('Nom d\'usuari: ')
            username = input(input_msg).encode('utf-8')

            try:
                Usuari._default_manager.db_manager(database).get(**{
                    username_field.name: username
                })
            except Usuari.DoesNotExist:
                break
            else:
                self.stderr.write("El correu electrònic ja està en ús. Si us plau, introdueix un altre.")

        # Solicitar los otros campos requeridos para el superusuario
        # Puedes usar input() o alguna otra forma para solicitar estos campos

        # Crear el superusuario utilizando el modelo personalizado 'Usuari'
        # Asegúrate de validar los campos requeridos y guardar el superusuario correctamente
        # Aquí hay un ejemplo básico de cómo podría ser:
        first_name = input("Nom: ").encode('utf-8')
        last_name = input("Cognoms: ")
        correu_ieti = input("Correu electrònic IETI: ").encode('utf-8')
        while True:
            try:
                fecha_nacimiento = input("Any de naixement (dia-mes-any -> 15-08-2000): ")
                any_naixement = datetime.datetime.strptime(fecha_nacimiento, "%d-%m-%Y")
                break
            except ValueError:
                print("Formato de fecha incorrecto. Por favor, utiliza el formato especificado (dia-mes-any).")
                
        password = getpass("Contrasenya: ").encode('utf-8')
        password_repeat = getpass("Contrasenya: ").encode('utf-8')

        try:
            if password != password_repeat:
                raise CommandError("Les contrasenyes no coincideixen.")
        except CommandError as e:
            self.stderr.write(self.style.ERROR(e))

        nou_usuari = Usuari.objects.create_user(username=username, correu_ieti=correu_ieti, password=password, nom=first_name, cognoms=last_name, any_naixement=any_naixement, tipus='super-usuari', is_staff=True, is_superuser=True)

        self.stdout.write(self.style.SUCCESS(f'Superusuari creat correctament amb el correu "{correu_ieti}".'))

        # Puedes agregar más lógica aquí si necesitas realizar alguna acción adicional después de crear el superusuario