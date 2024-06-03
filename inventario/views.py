from django.shortcuts import render, get_object_or_404, redirect
from .models import Inventario
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import InventarioForm, ActualizarInventarioForm
from django.contrib import messages

# Create your views here.

@login_required
def inventario_lista(request):
    query = request.GET.get('q')
    inventarios = Inventario.objects.all()

    if query:
        inventarios = inventarios.filter(nombre__icontains=query)

    context = {
        'titulo': 'Lista de Inventarios',
        'inventarios': inventarios
    }
    return render(request, 'inventario/lista_inventario.html', context=context)

@login_required
def producto_inventario(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    context = {
        'inventario': inventario
    }
    return render(request, 'inventario/producto.html', context=context)

@login_required
def agg_inventario(request):
    if request.method == "POST":
        agregar_form = InventarioForm(request.POST)
        if agregar_form.is_valid():
            nuevo_inventario = agregar_form.save(commit=False)
            nuevo_inventario.ventas = float(agregar_form.cleaned_data['precio']) * float(agregar_form.cleaned_data['cantidad_vendida'])
            nuevo_inventario.save()
            messages.success(request, "Agregado Exitosamente al Inventario!!")
            return redirect("/inventario/")
    else:
        agregar_form = InventarioForm()
    
    return render(request, 'inventario/agregar_inventario.html', {'form': agregar_form})

@login_required
def eliminar_inventario(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    inventario.delete()
    messages.error(request, "¡Inventario borrado exitosamente!")
    return redirect("/inventario/")

@login_required
def actualizar_inventario(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)

    if request.method == "POST":
        actualizar_form = ActualizarInventarioForm(request.POST)
        if actualizar_form.is_valid():
            inventario.nombre = actualizar_form.cleaned_data['nombre']
            inventario.cantidad_existente = actualizar_form.cleaned_data['cantidad_existente']
            inventario.cantidad_vendida = actualizar_form.cleaned_data['cantidad_vendida']
            inventario.precio = actualizar_form.cleaned_data['precio']
            inventario.ventas = float(inventario.precio) * float(inventario.cantidad_vendida)
            inventario.save()
            messages.success(request, "Actualizado Exitosamente al Inventario!!")
            return redirect(f"/inventario/producto_inventario/{pk}")
    else:
        actualizar_form = ActualizarInventarioForm(instance=inventario)

    context = {
        'form': actualizar_form
    }
    return render(request, 'inventario/actualizar_inventario.html', context=context)