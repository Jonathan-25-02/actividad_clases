# Create your models here.
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Dispositivo(models.Model):
    TIPO_CHOICES = [
        ('Laptop', 'Laptop'),
        ('Smartphone', 'Smartphone'),
        ('Tablet', 'Tablet'),
        ('Otro', 'Otro'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    sistema_operativo = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='dispositivos')
    fecha_autorizacion = models.DateField()

    def __str__(self):
        return f"{self.tipo} - {self.modelo}"
