# Generated by Django 4.0.6 on 2022-11-15 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_tareas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventariodebodega',
            name='ingreso',
        ),
    ]
