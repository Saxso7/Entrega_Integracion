from django.urls import path
from . import views


urlpatterns = [
    path('lista_envio',views.envio, name='ver envio'),
    path('lista_envio/<int:nroSeguimiento>',views.envio,name='ver envio<rut>'),
    path('lista_envio/<int:nroSeguimiento>',views.envio,name='eliminar envio <id>'),
    path('lista_entrega',views.entrega, name='lista_entrega'),
    path('lista_entrega/<int:nroSeguimiento>',views.entrega, name='lista_entrega'),
    path('lista_entrega/<int:nroSeguimiento>',views.entrega,name='eliminar entrega <id>')
]
