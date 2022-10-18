from unittest.util import _MAX_LENGTH
from django.db import models



 #Create your models here.
class InventarioDeBodega(models.Model):
    id= models.AutoField(primary_key = True)
    columnas = models.IntegerField(verbose_name='Columnas')
    filas = models.IntegerField(verbose_name='Filas')
    bloque = models.CharField(max_length=200,verbose_name='Bloque')
    ContenidosInv = models.CharField(max_length=200, verbose_name='cont', default='N/A')
 



class Tareas(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=400,verbose_name='Nombre')
    IdTrabajador = models.CharField(max_length=200,verbose_name='IdTrbajador')
    Descripcion = models.CharField(max_length=800,verbose_name='Descripcion')
    Estado = models.BooleanField(verbose_name='Estado')


