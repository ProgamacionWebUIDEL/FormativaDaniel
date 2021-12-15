from django.contrib import admin

from .models import Veterinaria
from .models import Mascota
from .models import Comida

# Register your models here.
admin.site.register(Veterinaria)
admin.site.register(Mascota)
admin.site.register(Comida)