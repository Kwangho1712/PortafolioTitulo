from django import forms
from django.forms.widgets import TextInput
from .models import Producto, Proveedor, Cliente, FamiliaProducto, TipoProducto
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ["rut","nombre","telefono","email","direccion","rubro"]

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
        

class CustomUserCreationForm(UserCreationForm): 
    pass
    class Meta:
            model = User
            fields = ["username","email","password1","password2","is_superuser",]
            labels = {'is_superuser': 'Admin'}
            

class CustomUserChangeForm(UserChangeForm): 
    password = None
    class Meta:
        model = User
        fields = ["username","email","is_superuser"]
        labels = {'is_superuser': 'Admin'}

class CustomPasswordChangeForm(PasswordChangeForm):
    pass


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ["run","nombre","edad","fiar"]

        
        