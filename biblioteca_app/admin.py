from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class LogsAdmin(admin.ModelAdmin):
    list_display = ('tipus', 'titol', 'descripcio', 'data', 'usuari', 'pathname')
    list_filter = ('tipus', 'data', 'usuari', 'pathname')
    search_fields = ('tipus', 'titol', 'descripcio', 'data', 'usuari', 'pathname')
    date_hierarchy = 'data'
    ordering = ('data',)

admin.site.register(Logs, LogsAdmin)