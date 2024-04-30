from django.http import JsonResponse
from .models import *
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

@api_view(['POST'])
def create_log(request):
    try:
        log = Logs.objects.create(
            tipus = request.data.get('type'),
            titol = request.data.get('title'),
            descripcio = request.data.get('description'),
            data = request.data.get('date'),
            usuari = Usuari.objects.get(id=request.user.id),
            pathname = request.data.get('pathname')
        )

        return JsonResponse({
                "status": "OK"
            }, safe=False)
    except Usuari.DoesNotExist as e:
        print('HA PETADO PORQUE EL USUARIO NO ESTÁ REGISTRADO O NO EXISTE?? ', e)
        return JsonResponse({
                'status': 'KO', 
                'message': "L'usuari no existeix o no está registrat."
            }, safe=False)
    except Exception as e:
        print('HA PETADO HA PETADO HA PETADO HA PETADO: ', e)
        return JsonResponse({
                'status': 'KO', 
                'message': str(e)
            }, safe=False)
    
@api_view(['POST'])
def is_user_superuser(request):
    try:
        user = Usuari.objects.get(id=request.user.id)
        return JsonResponse({'status': 'OK', 'is_superuser': user.is_superuser}, safe=False)
    except NameError:
        return JsonResponse({'status': 'KO', 'message': "L'usuari no està registrat."}, safe=False)
    except Exception as e:
        return JsonResponse({'status': 'KO', 'message': str(e)}, safe=False)
    
@api_view(['POST'])
def create_prestec(request):
    # request.itemId
    pass