# Generated by Django 2.1.3 on 2018-11-08 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0005_auto_20181107_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mascota',
            old_name='idmascota',
            new_name='codigoMascota',
        ),
        migrations.RenameField(
            model_name='mascota',
            old_name='mascotaname',
            new_name='nombreMascota',
        ),
        migrations.RemoveField(
            model_name='mascota',
            name='raza',
        ),
        migrations.AddField(
            model_name='mascota',
            name='descripcionMascota',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='mascota',
            name='razaMascota',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='estado',
            field=models.CharField(max_length=20),
        ),
    ]
