from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from .models import *

# from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
# from django.contrib.auth.hashers import check_password
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# from .models import *

def loginView(request):
    data = {}
    if request.method == "POST":
        email = request.POST.get("email").lower()
        password = request.POST.get("password")
        try:
            user = Usuari.objects.get(email=email)
            if user is not None:
                login(request, user)
                # print(request.user)
                if user.is_superuser:
                    return redirect("dashboard/admin")
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

## VIEW PARA INICIAR SESION
# def loginView(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 if user.is_superuser:
#                     return redirect('admin_dashboard')  # Redirigir al dashboard del administrador
#                 else:
#                     return redirect('general_dashboard')  # Redirigir al dashboard del usuario general
#     else:
#         form = AuthenticationForm()
#     return render(request, 'landing_page.html', {'form': form})

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




