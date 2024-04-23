from django.http import JsonResponse
from .models import *
from rest_framework.decorators import api_view
# import json

@api_view(['POST'])
def create_log(request):
    print("deberia funcionar")
    # print(str(request))
    # for key, value in request.items():
    #     print(f'Key: {key}\nValue: {value}')
    # print(f"Variables de request:\n{vars(request)}")
    print(f'Request data: {request.data}')
    print(f'The title: {request.data.get("title")}')

    try:
        Logs.objects.create(
            tipus = request.data.get('type'),
            titol = request.data.get('title'),
            descripcio = request.data.get('description'),
            usuari = Usuari.objects.get(id=request.user.id),
            pathname = request.data.get('path')
        )

        return JsonResponse({
                "status": "OK"
            }, safe=False)
    except NameError:
        return JsonResponse({
                'status': 'KO', 
                'message': "L'usuari no està registrat."
            }, safe=False)
    except Usuari.DoesNotExist:
        return JsonResponse({
                'status': 'KO', 
                'message': "L'usuari no existeix."
            }, safe=False)
    except Exception as e:
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
