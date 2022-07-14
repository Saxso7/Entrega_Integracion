from os import stat
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from yaml import serialize
from .models import Envio,Entrega, Auth
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EnvioSerializers, EntregaSerializers, AuthUser
from rest_framework.parsers import JSONParser


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
    
'''class EntregaVista(View):
    
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
            return JsonResponse(datos)'''
    
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))    
def entrega(request):
    if request.method == 'GET':
        entregar = Entrega.objects.all()
        serializers = EntregaSerializers(entregar, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = EntregaSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Eliminar(APIView):
    
    def delete(self, request, id):
        eliminarEnvio = Envio.objects.get(id=id)
        eliminarEnvio.delete()
        datos = {'message':'eliminado con exito'}
        return JsonResponse(datos)

'''@api_view(['POST'])
def EntregaPost(request):
    serializer = EntregaSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)
    
class EntregaGet(APIView):
    
    serializer_class = EntregaSerializers
    
    def get(self,request, id=0):
        if(id > 0):
            entrega=Entrega.objects.filter(id=id).values()
            if len(entrega) > 0:
                entrega = entrega[0]
                datos = {'entrega':entrega}
            else:
                datos={'message':'id no encontrado'}
            return JsonResponse(datos)
                
            
        else:    
            entrega=Entrega.objects.all()
            if len(entrega)>0:
                datos={'entrega':entrega}
            else:
                datos={'message':'not found'}
            serializer=EntregaSerializers(entrega,many=True)  
            return Response(serializer.data)   
        '''
class EliminarEntrega(APIView):
    
    def delete(self, request, id):
        eliminarEntrega = Entrega.objects.get(id=id)
        eliminarEntrega.delete()
        datos = {'message':'eliminado con exito'}
        return JsonResponse(datos)

class Usuario(generics.ListCreateAPIView):
    queryset = Auth.objects.all()
    serializer_class = AuthUser
    