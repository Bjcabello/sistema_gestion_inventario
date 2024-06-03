from django.db import models

# Create your models here.
class Inventario(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    precio = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    cantidad_existente = models.IntegerField(null=False, blank=False)
    cantidad_vendida = models.IntegerField(null=False, blank=False)
    ventas = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    fecha_entrada = models.DateField(auto_now_add=True)
    fecha_salida = models.DateField(auto_now=True)
    
   
    def __str__(self) -> str:
        return self.nombre
    
    