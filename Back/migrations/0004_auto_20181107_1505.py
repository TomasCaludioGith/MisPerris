# Generated by Django 2.1.3 on 2018-11-07 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0003_mascota_raza'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='user',
        ),
        migrations.AddField(
            model_name='usuario',
            name='correo',
            field=models.CharField(default='asda@asda.cl', max_length=20),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default='123', max_length=20),
        ),
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default='', max_length=20),
        ),
    ]
