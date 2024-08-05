from django import forms
from .models import Inventario

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['nombre', 'precio', 'cantidad_existente', 'cantidad_vendida']

class ActualizarInventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['nombre', 'precio', 'cantidad_existente', 'cantidad_vendida']
