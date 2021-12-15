from enum import auto
from django.db.models import fields
from rest_framework import serializers
from .models import Veterinaria
from .models import Mascota
from .models import Comida


class VeterinariaSerializable(serializers.ModelSerializer):
    class Meta:
        model = Veterinaria 
        fields =(
            'nombre',
            'direccion',
            'numero_sucursales'
        )

class MascotaSerializable(serializers.ModelSerializer):
    class Meta:
        model = Mascota 
        fields =(
            'nombre',
            'Raza',
            'Color'
        )
class ComidaSerializable(serializers.ModelSerializer):
    class Meta:
        model = Comida
        fields =(
            'nombre',
            'Marca',
            'Precio'
        )
