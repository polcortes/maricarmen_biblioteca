from django.conf import settings
from django.shortcuts import render
from .forms import LoginForm


## VIEW PARA INICIAR SESION
def loginView(request):
    form = LoginForm()  # Crear una instancia del formulario de inicio de sesión
    return render(request, 'landing_page.html', {'form': form})
