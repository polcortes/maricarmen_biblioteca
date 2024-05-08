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
from django.urls import path, include, reverse_lazy
from biblioteca_app import views, api
from .views import import_csv

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.loginView, name='landing_page'),
    path('login/', views.loginView, name='login'),  # Definir la URL para el inicio de sesión
    path('api/create_log', api.create_log, ),
    path('dashboard/', views.dashboard, name='dashboard'),  # /dashboard/ que redirige a /dashboard/general/ o /dashboard/admin/ dependiendo del usuario o a '/' si no hay una sesión activa.
    path('dashboard/general/', views.general_dashboard, name='general_dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('profile/general/', views.general_profile, name='general_profile'),
    path('profile/admin/', views.admin_profile, name='admin_profile'),
    path('mostrar_usuaris/', views.mostrar_usuaris, name='mostrar_usuaris'),
    path('import_csv/', views.mostrar_importacion, name='mostrar_importacion'),
    path('editar_usuari/<int:usuario_id>/', views.editar_usuari, name='editar_usuari'),
    path('mostrar_crear_usuari/', views.mostrar_crear_usuario, name='mostrar_crear_usuario'),
    path('crear_usuari/', views.crear_usuari, name='crear_usuari'),
    # path('actualizar_list_users/<int:usuario_id>/', views.actualizar_list_users, name='actualizar_list_users'),
    path('change_pass/', views.change_pass, name='change_pass'),
    path('logout/', views.logout_view, name='logout'),
    path('cambiar-contrasenya/', views.cambiar_contrasenya, name='cambiar_contrasenya'),
    path('search/', views.search_results, name='search_results'),
    path('autocomplete/', views.autocomplete, name='autocomplete'),
    path('actualizar-datos/', views.actualizar_datos, name='actualizar_datos'),
    path('actualizar-datos-user/', views.actualizar_datos_usuario, name='actualizar_datos_usuario'),
    # path('importacion/', import_csv, name='importacion'),
    path('importacio/', import_csv, name='importacio'),
    path('admin_prestecs/', views.admin_prestecs, name='admin_prestecs'),
    path('api/createPrestec/', api.create_prestec, name='create_prestec'),
    path('llistat_prestecs/', views.llistat_prestecs, name='llistat_prestecs'),
    # path('recuperar_contrasenya/', views.recuperar_contrasenya, name='recuperar_contrasenya'),
    path('forgot_password/', auth_views.PasswordResetView.as_view(), name='forgot_password'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('login')), name="password_reset_confirm"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
]
