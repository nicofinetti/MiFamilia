from django.db import models

# Create your models here.
class Familiar(models.Model):
    puesto=models.CharField(max_length=40)
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni=models.IntegerField()
    fechaNacimiento=models.DateField()

