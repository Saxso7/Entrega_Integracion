from django.urls import path
#from . import views
from .views import search,inicio,index,Mapas,buscarEnvio

urlpatterns = [
    path('',inicio, name='inicio'),

    

    path('index',index,name='index'),
    path('maps',Mapas,name='mapa'),

    path('table',buscarEnvio, name='buscar'),
    
    path('search/',search,name="search")
]


#$ pip install -r requeriments.txt
#$ pip install -r .\requeriments.txt