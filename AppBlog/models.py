from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class Autos(models.Model):
    
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    año_de_fabricacion = models.IntegerField()
    descripcion = models.TextField(max_length=240, null=True, blank=True)
    imagen = models.ImageField(upload_to='imagenautos', null=True, blank=True)
    fecha_de_edicion = models.DateField()

    def __str__(self):

        return f" {self.marca} {self.modelo}" 


class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    
