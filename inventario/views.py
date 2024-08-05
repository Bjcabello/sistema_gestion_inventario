from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Inventario
from .forms import InventarioForm, ActualizarInventarioForm 



def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inventario_lista')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'registro/login.html')

@login_required
def inventario_lista(request):
    query = request.GET.get('q')
    inventarios = Inventario.objects.all()

    if query:
        inventarios = inventarios.filter(Q(nombre__icontains=query))

    context = {
        'titulo': 'Lista de Inventarios',
        'inventarios': inventarios
    }
    return render(request, 'inventario/lista_inventario.html', context)

@login_required
def producto_inventario(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    context = {
        'inventario': inventario
    }
    return render(request, 'inventario/producto.html', context)

@login_required
def agg_inventario(request):
    if request.method == "POST":
        agregar_form = InventarioForm(request.POST)
        if agregar_form.is_valid():
            nuevo_inventario = agregar_form.save(commit=False)
            nuevo_inventario.ventas = float(agregar_form.cleaned_data['precio']) * float(agregar_form.cleaned_data['cantidad_vendida'])
            nuevo_inventario.save()
            messages.success(request, "¡Agregado Exitosamente al Inventario!")
            return redirect("inventario_lista")
    else:
        agregar_form = InventarioForm()

    return render(request, 'inventario/agregar_inventario.html', {'form': agregar_form})

@login_required
def eliminar_inventario(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    inventario.delete()
    messages.success(request, "¡Inventario borrado exitosamente!")
    return redirect("inventario_lista")

@login_required
def actualizar_inventario(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)

    if request.method == "POST":
        actualizar_form = ActualizarInventarioForm(request.POST, instance=inventario)
        if actualizar_form.is_valid():
            inventario = actualizar_form.save(commit=False)
            inventario.ventas = float(inventario.precio) * float(inventario.cantidad_vendida)
            inventario.save()
            messages.success(request, "¡Actualizado Exitosamente el Inventario!")
            return redirect("producto", pk=pk)
    else:
        actualizar_form = ActualizarInventarioForm(instance=inventario)

    context = {
        'form': actualizar_form
    }
    return render(request, 'inventario/actualizar_inventario.html', context)

@login_required
def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')
    return redirect('homepage')
