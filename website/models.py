# Libraries and packages
from django.contrib.auth.models import AbstractUser
from django.db import models
from .choices import *

# Website models
class usuarios(AbstractUser):
    clave_de_cuenta = models.AutoField(primary_key = True, null = False)
    nombre = models.CharField(max_length = 30, null = False)
    correo = models.EmailField(unique = True, null = False)
    password = models.CharField(max_length = 16, null = False)

class perros(models.Model):
    clave_de_mascota = models.CharField(max_length = 30, primary_key = True, null = False)
    nombre = models.CharField(max_length = 30, null = False)
    fecha_de_nacimiento = models.DateField(null = False)
    raza = models.CharField(max_length = 3, choices = breeds, default = 'OTR', null = False)
    sexo = models.CharField(max_length = 1, choices = sex, default = 'H', null = False)
    clave_de_cuenta = models.ForeignKey(usuarios, on_delete = models.CASCADE)

class gramajes(models.Model):
    nombre_producto = models.CharField(max_length = 50, null = True, default = 'SIN-NOMBRE')
    gramaje = models.FloatField(null = False)
    fecha_de_calculo = models.DateField(auto_now_add = True, null = False)
    clave_de_mascota = models.ForeignKey(perros, on_delete = models.CASCADE)