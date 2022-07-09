from django.urls import path
from . import views

urlpatterns = [
    path('envioGet',views.EnvioGet.as_view(), name='ver'),
    path('envioGet/<int:rut>',views.EnvioGet.as_view(),name='ver<rut>'),
    path('envioPost',views.EnvioVistaPost.as_view(), name='crear'),
    path('envioDelete/<int:id>',views.Eliminar.as_view(),name='eliminar')

]
