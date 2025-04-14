from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)   
    class Meta:
        db_table = 'roles'
    
    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    
    class Meta:
        db_table = 'usuarios'
    
    def __str__(self):
        return self.username