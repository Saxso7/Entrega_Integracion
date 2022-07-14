from django.db import models
from django.utils import timezone
# Create your models here.

class Envio(models.Model):
    nroSeguimiento=models.AutoField(primary_key=True,auto_created=True,verbose_name='ID')
    nombre=models.CharField(max_length=50)
    rut=models.IntegerField()
    direccion=models.CharField(max_length=60)
    cantidad=models.IntegerField()
    precio=models.IntegerField()

    class Meta:
        db_table = 'envio'

    def __str__(self):
        return self.nroSeguimiento

class Entrega(models.Model):
    nroSeguimiento=models.AutoField(primary_key=True,auto_created=True,verbose_name='ID')
    nombre=models.CharField(max_length=50)
    rut=models.IntegerField()
    direccion=models.CharField(max_length=60)
    producto=models.CharField(max_length=20)
    cantidad=models.IntegerField()
    precio=models.IntegerField()
    cargoEntrega=models.IntegerField()
    entregaRealizada=models.CharField(max_length=2)

    class Meta:
        db_table = 'entrega'

    def __str__(self):
        return self.nroSeguimiento