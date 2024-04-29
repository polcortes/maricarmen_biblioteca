from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class LogsAdmin(admin.ModelAdmin):
    list_display = ('tipus', 'titol', 'descripcio', 'data', 'usuari', 'pathname')
    list_filter = ('tipus', 'data', 'usuari', 'pathname')
    search_fields = ('tipus', 'titol', 'descripcio', 'data', 'usuari', 'pathname')
    date_hierarchy = 'data'
    ordering = ('data',)

class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'tipus', 'centre')
    list_filter = ('is_staff', 'is_active', 'tipus',)

admin.site.register(Usuari, UsersAdmin)

admin.site.register(Logs, LogsAdmin)