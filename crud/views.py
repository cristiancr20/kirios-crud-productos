from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria, Marca
from .forms import ProductoForm, CategoriaForm, MarcaForm, FacturaForm, DetalleFacturaForm

from django.http import HttpResponseNotAllowed, JsonResponse
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

#PRODUCTOS

def crear(request):
    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('crud:crearProducto')
    else:
        form = ProductoForm()
    
    return render(request, 'crearProductos.html', {'form': form, 'marcas': marcas, 'categorias': categorias})

def editar(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precioVenta = request.POST.get('precioVenta')
        precioCompra = request.POST.get('precioCompra')
        estado = request.POST.get('estado')
        stock = request.POST.get('stock')
        producto.nombre = nombre
        producto.precioVenta = precioVenta
        producto.precioCompra = precioCompra
        producto.estado = estado
        producto.stock = stock
        producto.save()
        return redirect('crud:verProducto')
    return render(request, 'editarProducto.html', {'producto': producto})

def eliminar(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('crud:verProducto')
    return render(request, 'confirmacionEliminar.html', {'producto': producto})

def ver(request):
    productos = Producto.objects.all().order_by('id')
    return render(request, 'verProducto.html', {'productos': productos})


#CATEGORIAS
def crearCategoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:crearCategoria')
    else:
        form = CategoriaForm()
    
    return render(request, 'crearCategoria.html', {'form': form})

def editarCategoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        categoria.nombre = nombre
        categoria.save()
        return redirect('crud:verCategoria')
    return render(request, 'editarCategoria.html', {'categoria': categoria})

def eliminarCategoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'POST':
        categoria.delete()
        return redirect('crud:verCategoria')   
    return render(request, 'confirmarEliminarCategoria.html', {'categoria': categoria})
    
def verCategoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'verCategoria.html', {'categorias': categorias})


#MARCAS
def crearMarca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:crearMarca')
    else:
        form = MarcaForm()
    
    return render(request, 'crearMarca.html', {'form': form})

def editarMarca(request, id):
    marca = Marca.objects.get(id=id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        estado = request.POST.get('estado')
        marca.nombre = nombre
        marca.estado = estado
        marca.save()
        return redirect('crud:verMarca')
    return render(request, 'editarMarca.html', {'marca': marca})

def eliminarMarca(request, id):
    marca = get_object_or_404(Marca, id=id)
    
    if request.method == 'POST':
        marca.delete()
        return redirect('crud:verMarca')
    return render(request, 'confirmarEliminarMarca.html', {'marca': marca})

def verMarca(request):
    marcas = Marca.objects.all()
    return render(request, 'verMarca.html', {'marcas': marcas})


#FACTURAS
def crearFactura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:crearFactura')
    else:
        form = FacturaForm()
    
    return render(request, 'crearFactura.html', {'form': form})

def crearDetalleFactura(request):
    if request.method == 'POST':
        form = DetalleFacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:crearFactura')
    else:
        form = DetalleFacturaForm()
    
    return render(request, 'crearDetalleFactura.html', {'form': form})

def buscar_productos(request):
    query = request.GET.get('q', '')
    productos = Producto.objects.filter(nombre__icontains=query) if query else Producto.objects.all()
    productos_data = [{'id': p.id, 'nombre': p.nombre, 'precio':  str( p.precioVenta)} for p in productos]
    print(productos_data)
    return render(request, 'buscar_productos.html', {'productos': productos, 'query': query})

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})


def agregar_carrito(request, id):
    # Aquí puedes agregar la lógica para añadir el producto al carrito de compras
    producto = get_object_or_404(Producto, id=id)
    # Supongamos que tienes un método para agregar al carrito
    agregar_producto_al_carrito(request, producto)
    return JsonResponse({'message': 'Producto agregado al carrito'})

