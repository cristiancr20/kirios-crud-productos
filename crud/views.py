from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria, Marca, DetalleFactura, Factura
from .forms import ProductoForm, CategoriaForm, MarcaForm
from django.contrib import messages



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

def buscar_productos(request):
    query = request.GET.get('q', '')
    productos = Producto.objects.filter(nombre__icontains=query) if query else []
    
    factura = request.session.get('factura', {})
    if not isinstance(factura, dict):
        factura = {}
        request.session['factura'] = factura
    productos_factura = Producto.objects.filter(id__in=factura.keys())
    
    total_factura = sum(producto.precioVenta * factura[str(producto.id)] for producto in productos_factura)
    
    productos_factura_subtotal = {}
    for producto in productos_factura:
        cantidad = factura.get(str(producto.id), 0)
        subtotal = producto.precioVenta * cantidad
        productos_factura_subtotal[producto] = subtotal

    if request.method == 'POST':
        # Procesar el formulario para guardar la factura
        cliente = request.POST.get('cliente')
        fecha = request.POST.get('fecha')
        
        nueva_factura = Factura.objects.create(
            fecha=fecha,
            cliente=cliente,
            total=total_factura,
        )

        for producto in productos_factura:
            cantidad = factura[str(producto.id)]
            subtotal = productos_factura_subtotal[producto]
            DetalleFactura.objects.create(
                factura=nueva_factura,
                producto=producto,
                cantidad=cantidad,
                precio=producto.precioVenta,
                subtotal=subtotal
            )

            
        # Eliminar la factura de la sesión después de guardarla en la base de datos
        del request.session['factura']

        messages.success(request, 'La factura se ha guardado correctamente.')

    context = {
        'productos': productos,
        'query': query,
        'productos_factura': productos_factura,
        'factura': factura,
        'productos_factura_subtotal': productos_factura_subtotal,
        'total_factura': total_factura
    }
    
    return render(request, 'buscar_productos.html', context)

def agregar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    factura = request.session.get('factura', {})
    if not isinstance(factura, dict):
        factura = {}

    # Incrementar la cantidad del producto si ya está en la factura
    if str(producto_id) in factura:
        factura[str(producto_id)] += 1
    else:
        factura[str(producto_id)] = 1
    request.session['factura'] = factura
    return redirect('crud:buscar_productos')

def actualizar_cantidad(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    # Obtener la factura de la sesión
    factura = request.session.get('factura', {})
    if not isinstance(factura, dict):
        factura = {}
        request.session['factura'] = factura
    
    # Manejar la actualización de cantidad
    if request.method == 'POST':
        action = request.POST.get('action')
        cantidad = int(request.POST.get('cantidad'))
        if action == 'incrementar':
            factura[str(producto_id)] = cantidad + 1
        elif action == 'decrementar' and cantidad > 0:
            factura[str(producto_id)] = cantidad - 1
    
    # Guardar la factura actualizada en la sesión
    request.session['factura'] = factura

    return redirect('crud:buscar_productos')

from django.contrib import messages
from django.shortcuts import redirect
from .models import Factura, DetalleFactura, Producto

def guardar_factura(request):
    if request.method == 'POST':
        # Obtener los datos de la factura desde el formulario
        fecha = request.POST.get('fecha')
        cliente = request.POST.get('cliente')
        total = request.POST.get('total')

        # Validar los datos del formulario
        if not fecha or not cliente or not total:
            messages.error(request, 'Por favor, complete todos los campos del formulario.')
            return redirect('ruta_del_formulario')

        try:
            total = float(total)
        except ValueError:
            messages.error(request, 'El total debe ser un número válido.')
            return redirect('ruta_del_formulario')

        # Crear una nueva instancia de Factura y guardarla en la base de datos
        nueva_factura = Factura.objects.create(
            fecha=fecha,
            cliente=cliente,
            total=total
        )

        # Obtener los productos de la factura desde la sesión
        factura = request.session.get('factura', {})
        if not isinstance(factura, dict):
            factura = {}
            request.session['factura'] = factura

        productos_factura = Producto.objects.filter(id__in=factura.keys())

        # Guardar los detalles de la factura en la base de datos
        detalles_factura = []
        for producto in productos_factura:
            cantidad = factura[str(producto.id)]
            precio = producto.precioVenta
            subtotal = precio * cantidad
            detalle_factura = DetalleFactura.objects.create(
                factura=nueva_factura,
                producto=producto,
                cantidad=cantidad,
                precio=precio,
                subtotal=subtotal
            )
            detalles_factura.append(detalle_factura)

            # Actualizar el stock del producto
            producto.stock -= cantidad
            producto.save()

        # Limpiar la sesión de la factura
        del request.session['factura']

        messages.success(request, 'La factura se ha guardado correctamente.')
        return redirect('crud:buscar_productos')

    # Si el método de la solicitud no es POST, redireccionar a alguna vista o plantilla adecuada.
    return redirect('crud:buscar_productos')


def ver_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'verFacturas.html', {'facturas': facturas})

def ver_detalle_factura(request, factura_id):
    detalles = DetalleFactura.objects.filter(factura_id=factura_id)
    return render(request, 'verDetalleFactura.html', {'detalle_factura': detalles})

def eliminar_factura(request, factura_id):
    factura = Factura.objects.get(id=factura_id)
    factura.delete()
    return redirect('crud:ver_facturas')
