from email import message
import json
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from yaml import serialize
from .models import Envio,Entrega
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EnvioSerializers, EntregaSerializers

# Create your views here.

class EnvioGet(APIView):
    serializer_class = EnvioSerializers
    
    def get(self,request, rut=0):
        if(rut > 0):
            envio=Envio.objects.filter(rut=rut).values()
            if len(envio) > 0:
                envios = envio[0]
                datos = {'envio':envios}
            else:
                datos={'message':'rut no encontrado'}
            return JsonResponse(datos)
                
            
        else:    
            envio=Envio.objects.all()
            if len(envio)>0:
                datos={'envio':envio}
            else:
                datos={'message':'not found'}
            serializer=EnvioSerializers(envio,many=True)  
            return Response(serializer.data)   
 
    

            
  
class EnvioVistaPost(APIView):  
    serializer_class = EnvioSerializers
        
    def post(self, request, *args, **kwargs):
        envioCrear = request.data
        print(envioCrear)
        envioCreado = Envio.objects.create(nombre=envioCrear['nombre'],rut=envioCrear['rut'],direccion=envioCrear['direccion'],
                             nroSeguimiento=envioCrear['nroSeguimiento'],producto=envioCrear['producto'],
                             cantidad=envioCrear['cantidad'],precio=envioCrear['precio'])
        
        envioCreado.save()
        
        serializer = EnvioSerializers(envioCreado)
        
        return Response(serializer.data)
    
class EntregaVista(View):
    
    def get(self, request, id=0):
        if(id > 0):
            entrega=list(Entrega.objects.filter(id=id).values())
            if len(entrega) > 0:
                entrega = entrega[0]
                datos = {'entrega':entrega}
            else:
                datos={'entrega':entrega}
            return JsonResponse(datos)
        else:    
            entrega=list(Entrega.objects.values())
            if len(entrega)>0:
                datos={'entrega':entrega}
            else:
                datos={'message':'not found'}
            return JsonResponse(datos)
    
class Eliminar(APIView):
    
    def delete(self, request, id):
        eliminarEnvio = Envio.objects.get(id=id)
        eliminarEnvio.delete()
        datos = {'message':'eliminado con exito'}
        return JsonResponse(datos)
    