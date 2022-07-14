from django.urls import path
from . import views


urlpatterns = [
    path('envioGet',views.EnvioGet.as_view(), name='ver envio'),
    path('envioGet/<int:nroSeguimiento>',views.EnvioGet.as_view(),name='ver envio<rut>'),
    path('envioPost',views.EnvioVistaPost.as_view(), name='crear envio'),
    path('envioDelete/<int:nroSeguimiento>',views.EliminarEnvio.as_view(),name='eliminar envio <id>'),
    path('lista_entrega',views.entrega, name='lista_entrega'),
    path('lista_entrega/<int:nroSeguimiento>',views.entrega, name='lista_entrega'),
    path('lista_entrega/<int:nroSeguimiento>',views.entrega,name='eliminar entrega <id>')
]
