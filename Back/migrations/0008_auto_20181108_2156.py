# Generated by Django 2.1.3 on 2018-11-09 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0007_auto_20181108_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mascota',
            old_name='idMascota',
            new_name='codigoMascota',
        ),
        migrations.RenameField(
            model_name='mascota',
            old_name='generomascota',
            new_name='descripcionMascota',
        ),
        migrations.RenameField(
            model_name='mascota',
            old_name='mascotaname',
            new_name='nombreMascota',
        ),
        migrations.RenameField(
            model_name='mascota',
            old_name='raza',
            new_name='razaMascota',
        ),
    ]
