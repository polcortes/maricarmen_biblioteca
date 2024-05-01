from django.http import JsonResponse
from .models import *
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.db.models import F

from datetime import datetime, timedelta

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
    user = request.user
    itemId = request.data.get('itemId')
    print(f"User: {user}. itemId: {itemId}")
    # try:
    item = ItemCataleg.objects.get(id_cataleg=itemId)

    if item.exemplars > 0:
        prestec = Prestecs.objects.create(
            item_cataleg = item,
            usuari = user,
            data_prestec = datetime.now(),
            data_limit = datetime.now() + timedelta(days=30),
            data_retorn = None
        )

        prestec.save()

        ItemCataleg.objects.filter(id_cataleg=itemId).update(exemplars=F('exemplars')-1)

        Logs.objects.create(
            tipus = 'info',
            titol = 'Prestec creat',
            descripcio = f'L\'usuari amb l\'id {user.id} ha agafat en préstec l\'item amb l\'id {item.id_cataleg}.',
            data = datetime.now(),
            usuari = user,
            pathname = '/search/'
        )
        return JsonResponse({'status': 'OK'}, safe=False)
    else:
        Logs.objects.create(
            tipus = 'info',
            titol = 'Error en create_prestec',
            descripcio = f"No hi ha exemplars de l'item amb l'id {item.id_cataleg}.",
            data = datetime.now(),
            usuari = user,
            pathname = '/search/'
        )
        return JsonResponse({'status': 'KO', 'message': "L'item no existeix."}, safe=False)
    # except ItemCataleg.DoesNotExist as e:
    #     Logs.objects.create(
    #         tipus = 'info',
    #         titol = 'Error en create_prestec',
    #         descripcio = f"L'item no existeix. ID aconseguit: {itemId}",
    #         data = datetime.now(),
    #         usuari = user,
    #         pathname = '/search/'
    #     )
    #     return JsonResponse({'status': 'KO', 'message': "L'item no existeix."}, safe=False)
    # except Exception as e:
    #     Logs.objects.create(
    #         tipus = 'info',
    #         titol = 'Error en create_prestec',
    #         descripcio = str(e),
    #         data = datetime.now(),
    #         usuari = user,
    #         pathname = '/search/'
    #     )
    #     return JsonResponse({'status': 'KO', 'message': str(e)}, safe=False)