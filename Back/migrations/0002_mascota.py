# Generated by Django 2.1.3 on 2018-11-07 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('idmascota', models.AutoField(primary_key=True, serialize=False)),
                ('mascotaname', models.CharField(max_length=20)),
                ('estado', models.CharField(default='Rescatado', max_length=20)),
            ],
        ),
    ]
