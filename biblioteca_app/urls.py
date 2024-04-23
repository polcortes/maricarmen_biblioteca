"""maricarmen_biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from biblioteca_app import views, api
from . import views

urlpatterns = [
    path('', views.loginView, name='landing_page'),
    path('login/', views.loginView, name='login'),  # Definir la URL para el inicio de sesión
    path('api/create_log', api.create_log, ),
    # path('api/login_api/', api.login_api, name='login_api'),
    path('dashboard/general/', views.general_dashboard, name='general_dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('change_pass/', views.change_pass, name='change_pass'),
    path('search_results/', views.change_pass, name='change_pass'),
    path('logout/', api.logout_view, name='logout'),
    path('cambiar-contrasenya/', api.cambiar_contrasenya, name='cambiar_contrasenya'),
    path('search/', views.search_results, name='search_results'),
    path('autocomplete/', views.autocomplete, name='autocomplete'),

]
