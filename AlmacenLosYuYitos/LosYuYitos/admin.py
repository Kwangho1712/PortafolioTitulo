from django.contrib import admin
from .models import Proveedor, Cliente, Producto, TipoProducto, FamiliaProducto

# Register your models here.

admin.site.register(Proveedor)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(TipoProducto)
admin.site.register(FamiliaProducto)