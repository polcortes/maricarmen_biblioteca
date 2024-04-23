from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib import admin
# from .models import Usuari, Cataleg

# Create your models here.
    
class ItemCataleg(models.Model):
    id_cataleg = models.AutoField(primary_key=True, unique=True)
    titol = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    descripcio = models.TextField()
    lloc_edicio = models.CharField(max_length=100)
    any = models.IntegerField()
    pais = models.CharField(max_length=100)
    signatura = models.CharField(max_length=100)
    exemplars = models.IntegerField()
    url = models.URLField()
    imatge = models.ImageField()
    mides = models.CharField(max_length=100)
    procedencia = models.CharField(max_length=100)
    caracteristiques = models.TextField()
    altra_informacio = models.TextField()

class Llibre(ItemCataleg):
    CDU = models.CharField(max_length=100)
    ISBN = models.IntegerField()
    editorial = models.CharField(max_length=100)
    colleccio = models.CharField(max_length=100)
    pagines = models.IntegerField()
    descriptors = models.CharField(max_length=100, blank=True) #TODO: Que es un descriptor?? (Se podria generar de manera automatica con el CDU)
    resum = models.TextField()
    volums = models.IntegerField()

class CD(ItemCataleg):
    discografia = models.CharField(max_length=100)
    estil = models.CharField(max_length=100)
    duracio = models.TimeField()

class DVD(ItemCataleg):
    discografia = models.CharField(max_length=100)
    estil = models.CharField(max_length=100)
    duracio = models.TimeField()

class BR(ItemCataleg):
    discografia = models.CharField(max_length=100)
    estil = models.CharField(max_length=100)
    duracio = models.TimeField()

class Dispositiu(ItemCataleg):
    marca = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    capacitat = models.CharField(max_length=100)
    bateria = models.CharField(max_length=100)


# TODO: Peta al crear un superuser:
class Usuari(AbstractUser):
    TYPE_OPTIONS = (
        ('alumne', 'Alumne'),
        ('professor', 'Professor'),
        ('admin', 'Admin'),
        ('super-usuari', 'Super Usuari')
    )

    is_superuser = models.BooleanField(default=False)
    username = models.CharField(max_length=100, unique=True)
    nom = models.CharField(max_length=100)
    cognoms = models.CharField(max_length=100)
    any_naixement = models.DateField(blank=False)
    email = models.EmailField(blank=False, unique=True)
    tipus = models.CharField(max_length=20, choices=TYPE_OPTIONS)
    password = models.CharField(max_length=128)

    def checkMail(self, mail):
        if '@iesesteveterradas.cat' in mail: return True
        return False
    
    def checkPass(self, password):
        return password == self.password

    def __str__(self) -> str:
        return f"{self.nom} {self.cognoms}"
    
class Prestecs(models.Model):
    usuari = models.ForeignKey(Usuari, on_delete=models.CASCADE)
    # cataleg = models.ForeignKey(Cataleg, on_delete=models.CASCADE, required=True)
    item_cataleg = models.ForeignKey(ItemCataleg, on_delete=models.CASCADE)
    data_prestec = models.DateTimeField()
    data_retorn = models.DateTimeField()
    data_limit = models.DateTimeField()
    # observacions = models.TextField()

    def __str__(self) -> str:
        return f"{self.usuari} ha agafat en préstec {self.item_cataleg}"
    
class Reserves(models.Model):
    usuari = models.ForeignKey(Usuari, on_delete=models.CASCADE,)
    item_cataleg = models.ForeignKey(ItemCataleg, on_delete=models.CASCADE,)
    data_reserva = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.usuari} ha reservat {self.item_cataleg}"
    
class Peticions(models.Model):
    usuari = models.ForeignKey(Usuari, on_delete=models.CASCADE, )
    text = models.TextField()
    is_accepted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.usuari} ha fet una petició de {self.text}"
    
class Logs(models.Model):
    TYPE_OPTIONS = (
        ('info', 'INFO'),
        ('warning', 'WARNING'),
        ('error', 'ERROR'),
        ('fatal', 'FATAL'),
    )

    tipus = models.CharField(max_length=100, choices=TYPE_OPTIONS,)
    titol = models.CharField(max_length=100, )
    descripcio = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    usuari = models.ForeignKey(Usuari, on_delete=models.CASCADE,)
    pathname = models.CharField(max_length=100, )

    def __str__(self) -> str:
        return f"{self.tipus} - {self.titol} - {self.data}"
    

#class UserAdmin(admin.ModelAdmin):
#    list_display = ('correu_ieti', 'first_name', 'last_name')
#    list_filter = ('is_staff', 'is_superuser')


#admin.site.unregister(Usuari)
#admin.site.register(Usuari, UserAdmin)

admin.site.register(ItemCataleg)
admin.site.register(Llibre)
admin.site.register(CD)
admin.site.register(DVD)
admin.site.register(BR)
admin.site.register(Dispositiu)

admin.site.register(Usuari)
admin.site.register(Prestecs)
admin.site.register(Reserves)
admin.site.register(Peticions)
# admin.site.register(Logs)