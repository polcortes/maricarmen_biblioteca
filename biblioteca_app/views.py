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


import json
import logging

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
            data['errorMsg'] = "L'usuari o la contrasenya són lalalalincorrectes."
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
    query = request.GET.get('query', '').strip()
    items = []
    if query:
        # Busca coincidencia exacta en lugar de coincidencias parciales
        items = ItemCataleg.objects.filter(titol__iexact=query)
    context = {
        'items': items,
        'query': query
    }
    return render(request, 'search_results.html', context)


def cambiar_contrasenya(request):
    # Obtener los datos del formulario
    current_password = request.data.get('current_password')
    new_password = request.data.get('new_password')

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
        
        # Actualizar los datos del usuario en la base de datos
        user = request.user
        user.nom = nom
        user.cognoms = cognoms
        user.save()

        isAdmin = request.user.is_staff
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
        isAdmin = request.user.is_staff
        if isAdmin:
            response = HttpResponse("""<script>window.location.href='/dashboard/admin?succ=0'; </script>""")
            return response
        else:
            response = HttpResponse("""<script>window.location.href='/dashboard/general?succ=0'; </script>""")
            return response
    
    
def editar_usuari(request, usuario_id):
    # Obtener el usuario a editar utilizando la ID pasada en la URL
    usuario = get_object_or_404(Usuari, pk=usuario_id)
    
    if request.method == 'POST':
        # Obtener los nuevos valores del formulario
        nom = request.POST.get('nom')
        cognoms = request.POST.get('cognoms')
        correu = request.POST.get('correu')
        
        # Actualizar los datos del usuario en la base de datos
        usuario.nom = nom
        usuario.cognoms = cognoms
        usuario.email = correu
        usuario.save()
        
        # Redirigir al usuario a la página de éxito o a la lista de usuarios
        # Cambia 'nombre_de_la_vista' al nombre de la vista donde deseas redirigir al usuario
        return redirect('mostrar_usuaris')

    # Pasar los datos del usuario a la plantilla para que los placeholders funcionen correctamente
    return render(request, 'edit_users.html', {'user_data': usuario})


# @login_required
# def actualizar_list_users(request, usuario_id):

#     print("usuario_id:", usuario_id)  # Imprimir el usuario_id para verificar si se está pasando correctamente

#     # Obtener el usuario correspondiente a partir de la ID proporcionada en la URL
#     usuario = get_object_or_404(Usuari, pk=usuario_id)
#     print("usuario:", usuario)  # Imprimir el usuario para verificar si se está encontrando correctamente

#     # Obtener el usuario correspondiente a partir de la ID proporcionada en la URL

#     if request.method == 'POST':
#         # Obtener los nuevos valores del formulario
#         nom = request.POST.get('nom')
#         cognoms = request.POST.get('cognoms')
#         correu = request.POST.get('correu')
        
#         # Verificar que la ID del usuario en la URL coincide con el usuario que se está modificando
#         if int(usuario_id) == usuario.id:
#             # Actualizar los datos del usuario en la base de datos
#             usuario.nom = nom
#             usuario.cognoms = cognoms
#             usuario.email = correu
#             usuario.save()

#             # Mostrar mensaje de éxito
#             messages.success(request, 'Los datos se han actualizado correctamente.')

#             # Redirigir al usuario a la página de la lista de usuarios
#             return redirect('mostrar_usuaris')
#         else:
#             # Si la ID del usuario en la URL no coincide con el usuario que se está modificando, mostrar un mensaje de error
#             messages.error(request, 'Error: No se puede modificar este usuario.')
#             return redirect('mostrar_usuaris')

#     # Si el método no es POST, simplemente renderiza la página con los datos actuales del usuario
#     return render(request, 'edit_users.html', {'usuario': usuario})  # Pasamos el objeto 'usuario' a la plantilla


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
    }
    return render(request, 'general_profile.html', {'user_data': user_data})

def admin_profile(request):
    # Obtener los datos del usuario actual desde la base de datos
    user = request.user
    user_data = {
        'nom': user.nom,
        'cognoms': user.cognoms,
        'correu': user.email,
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
    
    
    
def mostrar_usuaris(request):
    # Obtener los datos de los usuarios desde la base de datos o cualquier otra fuente
    usuarios = Usuari.objects.all()

    # Renderizar el contenido de usuarios utilizando una plantilla Django
    return render(request, 'list_users.html', {'usuarios': usuarios})


def mostrar_crear_usuario(request):
    return render(request, 'create_user.html')

