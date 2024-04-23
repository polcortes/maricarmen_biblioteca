from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from .models import Llibre, CD, DVD, BR, Dispositiu, ItemCataleg


## VIEW PARA INICIAR SESION
def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('admin_dashboard')  # Redirigir al dashboard del administrador
                else:
                    return redirect('general_dashboard')  # Redirigir al dashboard del usuario general
    else:
        form = AuthenticationForm()
    return render(request, 'landing_page.html', {'form': form})

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
