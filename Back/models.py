from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#manejo de usuarios perzonalizados
class Usuario(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #perfil=models.CharField(max_length=20,default=None)
    
#aqui tenemos los modelos lo que estaran presetes a la ora de pedir los usuario o mascotas


class Mascota (models.Model):

    idMascota=models.AutoField(primary_key=True)
    mascotaname=models.CharField(max_length=20, verbose_name="Nombre Mascota")
    raza=models.CharField(max_length=30,default="" ,verbose_name="Raza Mascota")
    foto = models.ImageField(upload_to="fotos/",verbose_name="Foto Mascota")
    generomascota=models.CharField(max_length=50,default="",verbose_name="Descripción")
    estado=models.CharField(max_length=20) 
    
