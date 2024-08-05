from django.urls import path
from .views import custom_login, inventario_lista, producto_inventario, agg_inventario, eliminar_inventario, actualizar_inventario, custom_logout

urlpatterns = [
    path('', custom_login, name='login'),  # Redirige a la vista de login personalizada al cargar la aplicación
    path('lista/', inventario_lista, name='inventario_lista'),
    path('producto_inventario/<int:pk>/', producto_inventario, name='producto'),
    path('agregar_inventario/', agg_inventario, name='agregar'),
    path('eliminar_inventario/<int:pk>/', eliminar_inventario, name='eliminar'),
    path('actualizar_inventario/<int:pk>/', actualizar_inventario, name='actualizar'),
    path('login/', custom_login, name='login'),  # Asegúrate de que esta también apunte a la vista personalizada
    path('logout/', custom_logout, name='logout'),
]
