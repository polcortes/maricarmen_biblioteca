from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from .models import Llibre, CD, DVD, BR, Dispositiu

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
def buscar_autocompletar(request):
    if 'term' in request.GET:
        query = request.GET.get('term')
        libros = Llibre.objects.filter(nombre__icontains=query)[:5]
        cds = CD.objects.filter(nombre__icontains=query)[:5]
        dvds = DVD.objects.filter(nombre__icontains=query)[:5]
        brs = BR.objects.filter(nombre__icontains=query)[:5]
        dispos = Dispositiu.objects.filter(nombre__icontains=query)[:5]
        results = list(libros.values('nombre')) + list(cds.values('nombre')) + list(dvds.values('nombre')) + list(brs.values('nombre')) + list(dispos.values('nombre'))
        titles = [result['nombre'] for result in results]
        return JsonResponse(titles, safe=False)
    return JsonResponse([], safe=False)

## VIEW RESULTADOS BUSQUEDA
def resultados_busqueda(request):
    query = request.GET.get('q', '')
    libros = Llibre.objects.filter(nombre__icontains=query)
    cds = CD.objects.filter(nombre__icontains=query)
    dvds = DVD.objects.filter(nombre__icontains=query)
    brs = BR.objects.filter(nombre__icontains=query)
    dispos = Dispositiu.objects.filter(nombre__icontains=query)
    return render(request, 'search_results.html', {'llibres': libros, 'cds': cds, 'dvds': dvds, 'brs': brs , 'dispo' : dispos, 'query': query})
