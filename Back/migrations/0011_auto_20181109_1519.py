# Generated by Django 2.1.3 on 2018-11-09 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0010_auto_20181108_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='perfil',
            field=models.CharField(default='', max_length=20),
        ),
    ]
