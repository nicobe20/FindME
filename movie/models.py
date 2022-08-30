from django.db import models

# Create your models here.
class InventarioBodega(models.Model):
    id= models.AutoField(primary_key = True)
    columnas = models.IntegerField(verbose_name='Columnas')
    filas = models.IntegerField(verbose_name='Filas')
    bloque = models.CharField(max_length=200,verbose_name='Bloque')




#hay que dropear la tabla y volverla hacer ya que tenemos que modificar unos valores y cambiarle el nombre, tambien la tenemos que volve
    


