# Generated by Django 4.0.6 on 2022-08-16 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_alter_inventariodebodega_bloque_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventariodebodega',
            name='columnas',
            field=models.CharField(max_length=300, verbose_name='Columnas'),
        ),
        migrations.AlterField(
            model_name='inventariodebodega',
            name='filas',
            field=models.CharField(max_length=300, verbose_name='Filas'),
        ),
    ]
