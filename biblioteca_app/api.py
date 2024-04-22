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
    except Exception as e:
        return JsonResponse({'status': 'KO', 'message': str(e)}, safe=False)
    

# ## VIEW CHANGE_PASS
# @login_required
# def cambiar_contrasenya(request):
#     if request.method == 'POST':
#         current_password = request.POST.get('current_password')
#         new_password = request.POST.get('new_password')

#         # Verificar la contraseña actual del usuario
#         if not request.user.check_password(current_password):
#             return JsonResponse({'error': 'La contrasenya actual no és vàlida.'}, status=400)

#         # Cambiar la contraseña del usuario
#         request.user.set_password(new_password)
#         request.user.save()

#         return JsonResponse({'message': 'Contrasenya canviada correctament.'})

#     return JsonResponse({'error': 'Només es permeten peticions POST.'}, status=405)