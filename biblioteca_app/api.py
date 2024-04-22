from django.http import JsonResponse
from .models import *
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


@api_view(['POST'])
def create_log(request):
    try:
        log = Logs()
        
        log.tipus = request.data.get('type')
        log.titol = request.data.get('title')
        log.descripcio = request.data.get('description')
        log.data = request.data.get('date')
        log.usuari = Usuari.objects.get(id=request.user.id)
        log.pathname = request.data.get('path')
        
        log.save()

        return JsonResponse({'status': 'OK'}, safe=False)
    except Exception as e:
        return JsonResponse({'status': 'KO', 'message': str(e)}, safe=False)
    

@api_view(['POST'])
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
    return redirect('landing_page.html') 
