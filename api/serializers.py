from rest_framework import serializers
from .models import Envio,Entrega

class EnvioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Envio
        fields = '__all__'

class EntregaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Entrega
        fields = '__all__'
        
