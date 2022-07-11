from django.urls import path
from . import views

urlpatterns = [
    path('envioGet',views.EnvioGet.as_view(), name='ver envio'),
    path('envioGet/<int:rut>',views.EnvioGet.as_view(),name='ver envio<rut>'),
    path('envioPost',views.EnvioVistaPost.as_view(), name='crear envio'),
    path('envioDelete/<int:id>',views.Eliminar.as_view(),name='eliminar envio <id>'),
    path('entregaGet',views.EntregaGet.as_view(),name='ver entrega'),
    path('entregaGet/<int:id>',views.EntregaGet.as_view(),name='ver entrega <id>'),
    path('entregaPost',views.EntregaPost.as_view(),name='crear envio'),
    path('entregaDelete/<int:id>',views.EliminarEntrega.as_view(),name='eliminar entrega <id>')
]
