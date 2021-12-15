from django.db import models

# Create your models here.
class Veterinaria(models.Model):
    nombre = models.CharField(max_length=120, help_text='Nombre del lugar')
    direccion = models.CharField(max_length=120, help_text='Direccion del lugar')
    numero_sucursales = models.IntegerField(max_length= 1000,help_text='Sucursales del lugar')

class Comida(models.Model):
    nombre = models.CharField(max_length=120, help_text='Nombre de la comida')
    Marca = models.CharField(max_length=120, help_text='Marca de la comida')
    Precio = models.IntegerField(max_length= 1000,help_text='Precio')
    

class Mascota(models.Model):
    nombre = models.CharField(max_length=120, help_text='Nombre del lugar')
    Raza= models.CharField(max_length=120, help_text='Raza de la mascota')
    Color= models.CharField(max_length=120, help_text='Color de la mascota')
    
    

