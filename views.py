from django.shortcuts import render
from rest_framework import viewsets
from .serializers import VeterinariaSerializable,MascotaSerializable,ComidaSerializable
from .models import Veterinaria
from .models import Mascota
from .models import Comida

# Create your views here.
class VeterinariaVista (viewsets.ModelViewSet):
    serializer_class:VeterinariaSerializable
    queryset = Veterinaria.objects.all()

class MascotaVista (viewsets.ModelViewSet):
    serializer_class:MascotaSerializable
    queryset = Mascota.objects.all()

class ComidaVista (viewsets.ModelViewSet):
    serializer_class:ComidaSerializable
    queryset = Comida.objects.all()


