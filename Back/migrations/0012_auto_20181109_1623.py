# Generated by Django 2.1.3 on 2018-11-09 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0011_auto_20181109_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='perfil',
            field=models.CharField(default=None, max_length=20),
        ),
    ]