from django.db import models

# Create your models here.

class Materia(models.Model):
    id_trabajador=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    curp=models.CharField(max_length=100)
    fecha_nacimiento=models.DateField((""), auto_now=False, auto_now_add=False)(max_length=100)
    puesto=models.CharField(max_length=100)
    salario=models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre