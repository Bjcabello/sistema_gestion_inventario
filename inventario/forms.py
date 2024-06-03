from django.forms import ModelForm
from .models import Inventario

class InventarioForm(ModelForm):
    class Meta:
        model = Inventario
        fields = ['nombre', 'precio', 'cantidad_existente', 'cantidad_vendida']

class ActualizarInventarioForm(ModelForm):
    class Meta:
        model = Inventario
        fields = ['nombre', 'precio', 'cantidad_existente', 'cantidad_vendida']