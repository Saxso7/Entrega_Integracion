from django.db import models

# Create your models here.
class Envio(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=60)
    nroSeguimiento=models.CharField(max_length=10)
    producto=models.CharField(max_length=20)
    cantidad=models.CharField(max_length=2)
    precio=models.CharField(max_length=8)
    
class Entrega(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=60)
    nroSeguimiento=models.CharField(max_length=10)
    producto=models.CharField(max_length=20)
    cantidad=models.CharField(max_length=2)
    precio=models.CharField(max_length=8)
    entregaRealizada=models.BooleanField()