from django.urls import path
from . import views

urlpatterns = [
    # Rutas para Historial (Cargos / Actividades)
    # Rutas para Usuario
    path('', views.usuarios),
    path('usuarios', views.usuarios),
    path('nuevoUsuario', views.nuevoUsuario),
    path('guardarUsuario', views.guardarUsuario),
    path('eliminarUsuario/<id>', views.eliminarUsuario),
    path('editarUsuario/<id>', views.editarUsuario),
    path('procesarEdicionUsuario/<id>', views.procesarEdicionUsuario),

    # Rutas para Dispositivo
    path('dispositivos', views.dispositivos),
    path('nuevoDispositivo', views.nuevoDispositivo),
    path('guardarDispositivo', views.guardarDispositivo),
    path('eliminarDispositivo/<id>', views.eliminarDispositivo),
    path('editarDispositivo/<id>', views.editarDispositivo),
    path('procesarEdicionDispositivo/<id>', views.procesarEdicionDispositivo),
]
