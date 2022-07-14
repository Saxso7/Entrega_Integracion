from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from rest_framework.authtoken.models import Token

import requests, json, MySQLdb

conexion = MySQLdb.connect(host='localhost', user='root', password= '*MySql1234',db='api',)

def index(request):
    url = 'http://127.0.0.1:8000/api/envioGet'
    response = requests.get(url)
    
    
            
    response_json = json.loads(response.content)
    print(response_json)
        
         
             
    return render(request, 'index.html',{
        'response_json': response_json,
        'despacho':'Pagina de despacho'
    })



def inicio(request):
    return render(request,'dashboard.html',{
        
    })
    
def Mapas(request):
    return render(request,'maps.html',{
        
    })

