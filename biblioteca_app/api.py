from django.http import JsonResponse
from .models import *
from rest_framework.decorators import api_view

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
    except NameError:
        return JsonResponse({'status': 'KO', 'message': "L'usuari no està registrat."}, safe=False)
    except Exception as e:
        return JsonResponse({'status': 'KO', 'message': str(e)}, safe=False)
    
@api_view(['POST'])
def is_user_superuser(request):
    try:
        user = Usuari.objects.get(id=request.user.id)
        return JsonResponse({'status': 'OK', 'is_superuser': user.is_superuser}, safe=False)
    except NameError:
        return JsonResponse({'status': 'KO', 'message': "L'usuari no està registrat."}, safe=False)
    except Exception as e:
        return JsonResponse({'status': 'KO', 'message': str(e)}, safe=False)