from django.db import models

# Create your models here.
class InventarioDeBodega(models.Model):
    id= models.AutoField(primary_key = True)
    columnas = models.IntegerField()
    filas = models.IntegerField()
    bloque = models.CharField(max_length=200)
    


