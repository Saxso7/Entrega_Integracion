from django.urls import path
from . import views

urlpatterns = [
    path('envio/get',views.EnvioGet.as_view(), name='ver'),
    path('envio/get/<int:id>',views.EnvioGet.as_view(),name='ver<id>'),
    path('envio/post',views.EnvioVistaPost.as_view(), name='crear')

]
