from django.contrib import admin
from .models import Envio,Entrega, Auth
# Register your models here.

admin.site.register(Envio)
admin.site.register(Entrega)
admin.site.register(Auth)