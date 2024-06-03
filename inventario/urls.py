from django.urls import path
from .views import inventario_lista, producto_inventario, agg_inventario, eliminar_inventario, actualizar_inventario

urlpatterns = [
    path('', inventario_lista, name='inventario_lista'), 
    path('producto_inventario/<int:pk>/', producto_inventario, name='producto'), 
    path('agregar_inventario/', agg_inventario, name='agregar'),
    path('eliminar_inventario/<int:pk>/', eliminar_inventario, name='eliminar'),
    path('actualizar_inventario/<int:pk>', actualizar_inventario, name='actualizar'),
]