from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('index.html',views.index,name='index'),
    path('maps.html',views.Mapas,name='mapa')
]
