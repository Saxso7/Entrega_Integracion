from os import stat
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from yaml import serialize
from .models import Envio,Entrega
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EnvioSerializers, EntregaSerializers


# Create your views here.

@csrf_exempt
@api_view(['GET','POST','DELETE'])   
def envio(request, nroSeguimiento=0):
    if request.method == 'GET':
        if(nroSeguimiento > 0):
            envio=Envio.objects.filter(nroSeguimiento=nroSeguimiento).values()
            if len(envio) > 0:
                envio = envio[0]
                datos = {'envio':envio}
            else:
                datos={'message':'nroSeguimiento no encontrado'}
            return JsonResponse(datos)
        else:    
            envio=Envio.objects.all()
            if len(envio)>0:
                datos={'envio':envio}
            else:
                datos={'message':'not found'}
            serializer=EnvioSerializers(envio,many=True)  
            return Response(serializer.data)
    elif request.method == 'POST':
        serializers = EnvioSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        eliminarEnvio = Envio.objects.get(nroSeguimiento=nroSeguimiento)
        eliminarEnvio.delete()
        datos = {'message':'eliminado con exito'}
        return JsonResponse(datos)
    
@csrf_exempt
@api_view(['GET','POST','DELETE'])   
def entrega(request, nroSeguimiento=0):
    if request.method == 'GET':
        if(nroSeguimiento > 0):
            entrega=Entrega.objects.filter(nroSeguimiento=nroSeguimiento).values()
            if len(entrega) > 0:
                entrega = entrega[0]
                datos = {'entrega':entrega}
            else:
                datos={'message':'nroSeguimiento no encontrado'}
            return JsonResponse(datos)
        else:    
            entrega=Entrega.objects.all()
            if len(entrega)>0:
                datos={'entrega':entrega}
            else:
                datos={'message':'not found'}
            serializer=EntregaSerializers(entrega,many=True)  
            return Response(serializer.data)
    elif request.method == 'POST':
        serializers = EntregaSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        eliminarEntrega = Entrega.objects.get(nroSeguimiento=nroSeguimiento)
        eliminarEntrega.delete()
        datos = {'message':'eliminado con exito'}
        return JsonResponse(datos)
