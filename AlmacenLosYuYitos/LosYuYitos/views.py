from django.contrib.auth.forms import AdminPasswordChangeForm, UserChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor, Cliente, Producto
from .forms import ClienteForm, CustomPasswordChangeForm, ProveedorForm, CustomUserCreationForm, CustomUserChangeForm, PasswordChangeForm, ProductoForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

# Create your views here.

@login_required
def listarProveedor(request):
    proveedores = Proveedor.objects.all()
    data = {
        'proveedores': proveedores
    }
    return render(request, 'app\Proveedor\ListarProveedor.html', data)

@login_required
@permission_required('LosYuyitos.add_proveedor')
def agregarProveedor(request):
    data = {
        'form': ProveedorForm()
    }

    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Proveedor Registrado")
        else:
            data["form"] = formulario
    return render(request, 'app\Proveedor\AgregarProveedor.html', data)

@login_required
@permission_required('LosYuyitos.change_proveedor')
def modificarProveedor(request, id):
    proveedor = get_object_or_404(Proveedor, rut=id)

    data = {
        'form': ProveedorForm(instance=proveedor)
    }

    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, instance=proveedor)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="/listarproveedor/")
        data["form"] = formulario
    return render(request, 'app\Proveedor\ModificarProveedor.html', data)

@login_required
@permission_required('LosYuyitos.delete_proveedor')
def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, rut=id)
    proveedor.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="/listarproveedor/")

@login_required
@permission_required('user.is_superuser')
def registroUsuario(request):

    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            # login(request, user)
            messages.success(request, "registro correcto")
            return redirect(to="listar-usuarios")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

@login_required
@permission_required('user.is_superuser')
def listarUsuarios(request):
        usuarios = User.objects.all()
        data = {
            'usuarios': usuarios
        }
        return render(request, 'registration/ListarUsuarios.html', data)

@login_required
@permission_required('user.is_superuser')
def eliminar_usuario(request, id):
    Usuario = User.objects.get(username=id)
    Usuario.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="/listarusuarios/")

@login_required
def agregar_cliente(request):
    data = {
        'form': ClienteForm()
    }

    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Cliente Registrado")
        else:
            data["form"] = formulario
    return render(request, 'app\Cliente\AgregarCliente.html', data)

@login_required
def listar_clientes(request):
    clientes = Cliente.objects.all()
    data = {
        'clientes': clientes
    }
    return render(request, 'app\Cliente\ListarCliente.html', data)

@login_required
def modificar_cliente(request, id):
    cliente = get_object_or_404(Cliente, run=id)

    data = {
        'form': ClienteForm(instance=cliente)
    }

    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="/listarcliente/")
        data["form"] = formulario
    return render(request, 'app\Cliente\ModificarCliente.html', data)

@login_required
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, run=id)
    cliente.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="/listarcliente/")


@login_required
@permission_required('user.is_superuser')
def editar_usuario(request, id):
    usuario = get_object_or_404(User, username=id)
    data = {
        'form': CustomUserChangeForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = CustomUserChangeForm(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="/listarusuarios/")
        data["form"] = formulario
        messages.warning(request, "Modificado INCorrectamente")
    return render(request, 'registration/ModificarUsuario.html', data)


@login_required
@permission_required('user.is_superuser')
def editar_password(request, id):
    usuario = get_object_or_404(User, username=id)
    if request.method == 'POST':
        form = PasswordChangeForm(usuario, request.POST)
        if form.is_valid():
            usuario = form.save()
            # update_session_auth_hash(request, usuario)
            messages.success(request, 'Cambio de contraseña exitoso')
            return redirect(to="/listarusuarios/")
        else:
            messages.error(request, 'Porfavor Correguir error')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/ModificarPassword.html', {
        'form': form
    })


@login_required
def agregarProducto(request):
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Registrado")
        else:
            data["form"] = formulario
    return render(request, 'app\Producto\AgregarProducto.html', data)

@login_required
def listarProducto(request):
        productos = Producto.objects.all()
        data = {
            'productos': productos
        }
        return render(request, 'app\Producto\ListarProducto.html', data)

@login_required
def modificar_producto(request, id):
    producto = get_object_or_404(Producto, cod_producto=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="/listarproductos/")
        data["form"] = formulario
    return render(request, 'app\Producto\ModificarProducto.html', data)

@login_required
def eliminar_producto(request, id):
    producto = Producto.objects.get(cod_producto=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="/listarproductos/")



