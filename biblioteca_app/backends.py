from django.contrib.auth.backends import BaseBackend
from .models import Usuari

class MyBackend(BaseBackend):
    def authenticate(self, request, mail=None, password=None):
        try:
            user = Usuari.objects.get(mail=mail)
            if user.checkMail(password) and user.checkPass(password):
                return user
        except Usuari.DoesNotExist:
            return None
        
    