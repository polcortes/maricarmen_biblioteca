from django.conf import settings
from django.shortcuts import render, redirect
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


def loginView(request):
    data = {}
    if request.method == "POST":
        email = request.POST.get("email").lower()
        password = request.POST.get("password")
        try:
            user = Usuari.objects.get(email=email)
            if user is not None and check_password(password, user.password):
                login(request, user)
                # print(request.user)
                if user.is_superuser:
                    return redirect("/admin") 
                elif user.is_staff:
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


## VIEW LOGOUT
def logout_view(request):
    logout(request)
    return redirect('landing_page.html')  # Cambia 'nombre_de_la_pagina_de_inicio' por el nombre de tu página de inicio

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