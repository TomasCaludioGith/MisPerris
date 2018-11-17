# Generated by Django 2.1.3 on 2018-11-12 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0015_auto_20181111_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(upload_to='fotos/', verbose_name='Foto Mascota'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='generomascota',
            field=models.CharField(default='', max_length=50, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='mascotaname',
            field=models.CharField(max_length=20, verbose_name='Nombre Mascota'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='raza',
            field=models.CharField(default='', max_length=30, verbose_name='Raza Mascota'),
        ),
    ]
