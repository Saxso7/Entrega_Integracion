from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.db.models import Q
from api import serializers
from api.models import Envio
from django.shortcuts import redirect
from django.contrib.auth import authenticate

import requests
import json
import MySQLdb


conexion = MySQLdb.connect(
    host='localhost', user='root', password='*MySql1234', db='api',)


def index(request):

    return render(request, 'main/index.html', {
        'despacho': 'Pagina de despacho'
    })


def buscarEnvio(request):
    ventas = Envio.objects.all()
    
    search = request.POST.get("busqueda")

    if (search):
        for v in ventas:
            if(v.nombre  == search):
                ventas = Envio.objects.filter(
                    Q(nombre__icontains = search)
                )


    
    
    

    return render(request, 'main/table.html' ,{'ventas': ventas})


def inicio(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            print("logueado correctamente")
            return redirect('index')

        else:
            print("Incorrecto")
    return render(request, 'main/login.html')


def Mapas(request):
    return render(request, 'main/maps.html', {

    })


def search(request):
    template_name = 'main/table.html'
    busqueda = request.GET["busqueda"]
    ventas = Envio.objects.filter(
        nombre__icontains=busqueda
    )
    data = {
        'ventas': ventas
    }

    return render(request, template_name, data)
