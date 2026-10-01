from django.db.models import ProtectedError
from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Producto
from .forms import CategoriaForm, ProductoForm


# ---------- Productos ----------
def lista_productos(request):
    productos = Producto.objects.select_related('categoria')
    return render(request, 'productos/lista.html', {'productos': productos})


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/formulario.html', {'form': form})


# ---------- Categorías ----------
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/lista.html', {'categorias': categorias})


def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/formulario.html',
                  {'form': form, 'titulo': 'Registrar categoría'})


def detalle_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    productos = categoria.productos.all()
    return render(request, 'categorias/detalle.html',
                  {'categoria': categoria, 'productos': productos})


def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('detalle_categoria', pk=categoria.pk)
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categorias/formulario.html',
                  {'form': form, 'titulo': 'Editar categoría'})


def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    error = None
    if request.method == 'POST':
        try:
            categoria.delete()
            return redirect('lista_categorias')
        except ProtectedError:
            error = ("No se puede eliminar: la categoría tiene productos "
                     "asociados. Elimina o reasigna esos productos primero.")
    return render(request, 'categorias/eliminar.html',
                  {'categoria': categoria, 'error': error})
