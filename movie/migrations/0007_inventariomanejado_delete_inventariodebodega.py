# Generated by Django 4.0.6 on 2022-08-17 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_inventariodebodega_delete_inventariobodega'),
    ]

    operations = [
        migrations.CreateModel(
            name='inventarioManejado',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('LoColumna', models.CharField(max_length=200, verbose_name='C')),
                ('LoFila', models.CharField(max_length=200, verbose_name='F')),
                ('Extra', models.CharField(max_length=200, verbose_name='E')),
            ],
        ),
        migrations.DeleteModel(
            name='InventarioDeBodega',
        ),
    ]
