from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from re import match
from django.db.models import Count

import datetime
import os
import json
import logging
from .forms import CSVUploadForm
from .models import Estudiante

import json
import csv

logger = logging.getLogger(__name__)

def loginView(request):
    data = {}
    if request.method == "POST":
        email = request.POST.get("email").lower()
        password = request.POST.get("password")
        try:
            user = Usuari.objects.get(email=email)
            print(user)
            if user is not None and check_password(password, user.password):
                login(request, user)
                print(request.user)
                if user.is_superuser:
                    return redirect("/admin") 
                if user.is_staff:
                    return redirect("dashboard/admin")                
                else:
                    return redirect("dashboard/general")
            else:
                data['error'] = True
                data['errorMsg'] = "L'usuari o la contrasenya són incorrectes."
        except:
            data['error'] = True
            data['errorMsg'] = "L'usuari o la contrasenya són incorrectes."
        # print(data)
    return render(request, "landing_page.html", data)
#pcortesgarcia.cf@iesesteveterradas.cat

## VIEW USER DASHBOARD 
# @login_required
def general_dashboard(request):
    return render(request, 'general_dashboard.html')

## VIEW ADMIN DASHBOARD
# @login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

## VIEW CHANGE PASSWD 
# @login_required
def change_pass(request):
    return render(request, 'change_pass.html')

## VIEW SEARCH RESULTS
# @login_required
def search_results(request):
    return render(request, 'search_results.html')


## VIEW AUTOCOMPLETAR
def autocomplete(request):
    query = request.GET.get('term', '')  # "term" es el parámetro que jQuery UI Autocomplete enviará
    if len(query) >= 3:
        items = ItemCataleg.objects.filter(titol__icontains=query)[:5]  # Limita a 5 resultados
        results = [{'label': item.titol, 'value': item.titol} for item in items]
    else:
        results = []
    return JsonResponse(results, safe=False)

## VIEW RESULTADOS BUSQUEDA
def search_results(request):
    query = request.GET.get('query', '').strip().lower()
    filters = {
        'tipus': request.GET.getlist('tipus'), # los checkboxes
        'editorial': request.GET.get('editorial', '').strip(),
        'llengua': request.GET.get('llengua', '').strip(),
        'centre': request.GET.get('centre', '').strip(),
        'data-edicio': request.GET.get('data-edicio', '').strip(),
    }

    # items = ItemCataleg.objects.filter(
    #     titol__icontains=query,
    #     llengua__icontains=filters['llengua'],
    #     centre__icontains=filters['centre'],
    # )

    items = ItemCataleg.objects.all()

    for item in items:
        print(item.tipus)

    if filters['tipus']:
        # items = items.annotate(num_tipus=Count('tipus'))
        # for tipus in filters['tipus']:
        #     items = items.filter(tipus=tipus.lower(), num_tipus__gt=0)
        for i in range(len(filters['tipus'])):
            filters['tipus'][i] = filters['tipus'][i].lower()
        items = items.filter(tipus__in=filters['tipus'])

    if query:
        items = items.filter(titol__icontains=query)
    
    if filters['llengua']:
        items = items.filter(llengua__icontains=filters['llengua'])
    
    if filters['centre']:
        items = items.filter(centre__icontains=filters['centre'])

    if 'Llibre' in filters['tipus']:
        items = items.filter(llibre__editorial__icontains=filters['editorial'],)

    # if filters['data-edicio']:
    #     for item in items:
    #         print(item.any)
    #         any = int(item.any)
    #         data_edicio = datetime.datetime(any, 1, 1)
    #         if (data_edicio > datetime.datetime(filters['data-edicio'].split(' - ')[0]) and data_edicio < datetime.datetime(filters['data-edicio'].split(' - ')[1])):
    #             items = items.filter(any=any)

    editorials = Llibre.objects.values('editorial').distinct()
    llengues = ItemCataleg.objects.values('llengua').distinct()
    centres = ItemCataleg.objects.values('centre').distinct()
    context = {
        'items': items,
        'query': query,
        'editorials': editorials,
        'llengues': llengues,
        'centres': centres,
    }
    return render(request, 'search_results.html', context)


def cambiar_contrasenya(request):
    # Obtener los datos del formulario
    current_password = request.data.get('current_password')
    new_password = request.data.get('new_password')

    check_pass_ok = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$'

    if not match(check_pass_ok, new_password): 
        return JsonResponse({ 
            'error': 'La nova contrasenya no conté almenys: 1 lletra minúscula, 1 lletra majúscula, 1 número, 1 caràcter especial i tenir una longitud de 8 a 16 caràcters.' 
        })

    # Verificar la autenticación del usuario
    user = authenticate(request, username=request.user.username, password=current_password)
    if user is None:
        return JsonResponse({'error': 'La contraseña actual es incorrecta'}, status=400)

    # Cambiar la contraseña
    user.set_password(new_password)
    user.save()

    return JsonResponse({'message': 'Contraseña cambiada exitosamente'})



def logout_view(request):
    logout(request)
    return redirect(reverse('landing_page')) 



def actualizar_datos(request):
    if request.method == 'POST':
        # Obtener los nuevos valores del formulario
        nom = request.POST.get('nom')
        cognoms = request.POST.get('cognoms')
        correu = request.POST.get('correu')
        
        # Actualizar los datos del usuario en la base de datos
        user = request.user
        user.nom = nom
        user.cognoms = cognoms
        user.email = correu
        user.save()

        isAdmin = request.user.is_superuser or request.user.is_staff
        if isAdmin:
            # Devolver una respuesta con un script de alerta en JavaScript
            response = HttpResponse("""<script>window.location.href='/dashboard/admin?succ=1'; </script>""")
            return response
        else:
            # Devolver una respuesta con un script de alerta en JavaScript
            response = HttpResponse("""<script>window.location.href='/dashboard/general?succ=1'; </script>""")
            return response
    else:
        # Devolver una respuesta con un script de alerta en JavaScript para el método no permitido
        #response = HttpResponse("""<script>window.history.back(); </script>""")
        #return response
        isAdmin = request.user.is_superuser or request.user.is_staff
        if isAdmin:
            response = HttpResponse("""<script>window.location.href='/dashboard/admin?succ=0'; </script>""")
            return response
        else:
            response = HttpResponse("""<script>window.location.href='/dashboard/general?succ=0'; </script>""")
            return response
    
def actualizar_datos_usuario(request):
    if request.method == 'POST':
        # Obtener los nuevos valores del formulario
        nom = request.POST.get('nom')
        cognoms = request.POST.get('cognoms')
        imatge_perfil = request.FILES.get('imatge_perfil')

        # Actualizar los datos del usuario en la base de datos
        user = request.user
        user.nom = nom
        user.cognoms = cognoms
        if imatge_perfil:
            # Guardar el archivo en la carpeta de medios
            user.imatge_perfil.save(imatge_perfil.name, imatge_perfil)
        user.save()

        if request.user.is_staff:
            messages.success(request, 'Dades actualitzades correctament!')
            return redirect('/dashboard/admin')
        else:
            messages.success(request, 'Dades actualitzades correctament!')
            return redirect('/dashboard/general')
    else:
        if request.user.is_staff:
            messages.error(request, 'Error en la actualització de les dades!')
            return redirect('/dashboard/admin')
        else:
            messages.error(request, 'Error en la actualització de les dades!')
            return redirect('/dashboard/general')
    
    
def editar_usuari(request, usuario_id):
    # Obtener el usuario a editar utilizando la ID pasada en la URL
    usuario = get_object_or_404(Usuari, pk=usuario_id)
    
    # Verificar si el usuario autenticado tiene el mismo centro que el usuario a editar
    if usuario.centre != request.user.centre:
        messages.error(request, 'No tienes permiso para editar este usuario.')
        return redirect('mostrar_usuaris')

    if request.method == 'POST':
        # Obtener los nuevos valores del formulario
        nom = request.POST.get('nom')
        cognoms = request.POST.get('cognoms')
        correu = request.POST.get('correu')
        any_naixement = request.POST.get('data')
        tipus = request.POST.get('tipus')
        
        # Actualizar los datos del usuario en la base de datos
        usuario.nom = nom
        usuario.cognoms = cognoms
        usuario.email = correu
        usuario.any_naixement = any_naixement
        usuario.tipus = tipus
        
        if tipus == 'admin':
            usuario.is_staff = True
        elif tipus == 'super-usuari':
            usuario.is_superuser = True
        
        usuario.save()
        
        # Redirigir al usuario a la página de éxito o a la lista de usuarios
        # Cambia 'nombre_de_la_vista' al nombre de la vista donde deseas redirigir al usuario
        return redirect('mostrar_usuaris')

    # Renderizar el formulario de edición
    return render(request, 'edit_users.html', {'user_data': usuario})







def mostrar_usuaris(request):
    # Obtener los datos de los usuarios desde la base de datos o cualquier otra fuente
    usuarios = Usuari.objects.all()

    # Renderizar el contenido de usuarios utilizando una plantilla Django
    return render(request, 'list_users.html', {'usuarios': usuarios})


def mostrar_crear_usuario(request):
    user = request.user
    user_data = {
        'centre': user.centre,
        'any_naixement' : user.any_naixement

    }
    return render(request, 'create_user.html', {'user_data': user_data})


def crear_usuari(request):
    if request.method == 'POST':
        nombre = request.POST.get('nom')
        apellidos = request.POST.get('cognoms')
        fecha_nacimiento = request.POST.get('any_naixement')
        email = request.POST.get('email')
        tipo = request.POST.get('tipus')
        password = request.POST.get('password')
        centro = request.POST.get('centre')

        # Comprobación de existencia de usuario con el mismo email
        if Usuari.objects.filter(email=email).exists():
            messages.error(request, 'El email ya está en uso.')
            return redirect('crear_usuari')

        # Encriptar la contraseña antes de guardarla
        hashed_password = make_password(password)

        # Creación del username
        username = f'{nombre}_{apellidos}'

        # Creación del usuario
        user = Usuari.objects.create(
            nom=nombre,
            cognoms=apellidos,
            any_naixement=fecha_nacimiento,
            email=email,
            tipus=tipo,
            password=hashed_password,
            centre=centro,
            username=username  # Añadimos el username aquí
        )

        # Personalización del usuario según el tipo
        # Aquí puedes añadir más lógica según los tipos de usuario
        if tipo == 'admin':
            user.is_staff = True
        elif tipo == 'super-usuari':
            user.is_superuser = True

        # Guardar el tipo de usuario
        user.save()

        # Mensaje de éxito
        messages.success(request, 'Usuario creado exitosamente.')

        # Redireccionar o renderizar otra página
        return redirect('mostrar_usuaris')  # Cambia 'mostrar_usuaris' por la URL a la que quieras redirigir después de crear el usuario

    # Si es un GET, renderizar la página de creación de usuario
    return render(request, 'create_user.html') 

def general_dashboard(request):
    return render(request, 'general_dashboard.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def general_profile(request):
    # Obtener los datos del usuario actual desde la base de datos
    user = request.user
    user_data = {
        'nom': user.nom,
        'cognoms': user.cognoms,
        'correu': user.email,
        'imatge_perfil': user.imatge_perfil,
        'any_naixement' : user.any_naixement
    }
    return render(request, 'general_profile.html', {'user_data': user_data})

def admin_profile(request):
    # Obtener los datos del usuario actual desde la base de datos
    user = request.user
    user_data = {
        'nom': user.nom,
        'cognoms': user.cognoms,
        'correu': user.email,
        'any_naixement' : user.any_naixement

    }
    return render(request, 'admin_profile.html', {'user_data': user_data})


def cambiar_contrasenya(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        # Verificar que la contraseña actual coincide con la del usuario
        user = request.user
        if not user.check_password(current_password):
            return JsonResponse({'error': 'La contraseña actual no es correcta'})

        # Verificar que las contraseñas nuevas tienen al menos 8 caracteres
        if len(new_password) < 8:
            return JsonResponse({'error': 'La nueva contraseña debe tener al menos 8 caracteres'})

        # Verificar que las contraseñas nuevas coinciden
        if new_password != confirm_password:
            return JsonResponse({'error': 'Las contraseñas nuevas no coinciden'})

        # Actualizar la contraseña del usuario en la base de datos
        user.password = make_password(new_password)
        user.save()

        return JsonResponse({'message': 'Contraseña cambiada exitosamente'})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
    
def mostrar_importacion(request):
    return render(request, 'importacion.html')
    

def import_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            reader = csv.reader(csv_file.read().decode('utf-8').splitlines())
            next(reader)  # Omitir la cabecera

            inserted_count = 0
            duplicate_count = 0
            line_number = 1  # Comenzar el conteo desde 1 después de la cabecera

            for row in reader:
                line_number += 1  # Incrementar antes de procesar para reflejar el número correcto de línea
                if not Estudiante.objects.filter(email=row[2]).exists():
                    try:
                        Estudiante.objects.create(
                            nom=row[0],
                            cognoms=row[1],
                            email=row[2],
                            telefon=row[3],
                            curs=row[4]
                        )
                        inserted_count += 1
                    except Exception as e:
                        error_type = type(e).__name__
                        error_message = str(e)
                        messages.error(request, f"Error al registre en la línea {line_number}")
                else:
                    duplicate_count += 1

            messages.success(request, f'Registres inserits correctament: {inserted_count}')
            if duplicate_count:
                messages.info(request, f'Registres duplicats no inserits: {duplicate_count}')

            return redirect('importacion')
    else:
        form = CSVUploadForm()
    return render(request, 'importacion.html', {'form': form})
