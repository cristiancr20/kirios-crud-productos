from django.shortcuts import render
from django.shortcuts import redirect

from .models import Producto, Categoria, Marca
from .forms import ProductoForm, CategoriaForm, MarcaForm

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
            form.save() # Redirigir a la vista de lista de productos
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
        producto.nombre = nombre
        producto.precioVenta = precioVenta
        producto.precioCompra = precioCompra
        producto.estado = estado
        producto.save()
        return redirect('index')
    return render(request, 'editar.html', {'producto': producto})

def eliminar(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('index')

def ver(request):
    productos = Producto.objects.all()
    return render(request, 'verProducto.html', {'productos': productos})


#CATEGORIAS
def crearCategoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('crud:verCategoria')
    else:
        form = CategoriaForm()
    
    return render(request, 'crearCategoria.html', {'form': form})

def editarCategoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        estado = request.POST.get('estado')
        categoria.nombre = nombre
        categoria.estado = estado
        categoria.save()
        return redirect('crud:verCategoria')
    return render(request, 'editarCategoria.html', {'categoria': categoria})

def eliminarCategoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('crud:verCategoria')
    

def verCategoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'verCategoria.html', {'categorias': categorias})


#MARCAS
def crearMarca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
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
        return redirect('index')
    return render(request, 'editarMarca.html', {'marca': marca})

def eliminarMarca(request, id):
    marca = Marca.objects.get(id=id)
    marca.delete()
    return redirect('index')

def verMarca(request):
    marcas = Marca.objects.all()
    return render(request, 'verMarca.html', {'marcas': marcas})




