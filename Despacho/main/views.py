from urllib import response
from django.shortcuts import render


import requests, json, MySQLdb

conexion = MySQLdb.connect(host='localhost', user='root', password= '*MySql1234',db='api2',)

def index(request):
    url = 'http://127.0.0.1:8000/api/envio/get'
    response = requests.get(url)
    
    
    if response.status_code == 200:
        
        recibido = True
        costo= 3000
        
        
        cur = conexion.cursor()
        cur.execute("SELECT nombre FROM api_envio")
        for nombre in cur.fetchall():
            print (nombre)
        conexion.close()
        
        response_json = json.loads(response.content)
        print(response_json)
        
        nombre = response_json[0]
        print(nombre)
        return render(request, 'index.html',{
            'response_json': response_json,
            'despacho':'Pagina de despacho'
        })
