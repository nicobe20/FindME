from django.db import models

# Create your models here.
class InventarioDeBodega(models.Model):
    id= models.AutoField(primary_key = True)
    columnas = models.IntegerField(verbose_name='Columnas')
    filas = models.IntegerField(verbose_name='Filas')
    bloque = models.CharField(max_length=200,verbose_name='Bloque')


    


