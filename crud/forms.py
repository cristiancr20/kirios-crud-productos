#forms.py 
from django import forms
from .models import Producto, Categoria, Marca, Factura, DetalleFactura


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precioVenta', 'precioCompra', 'marca', 'categoria', 'estado', 'stock']


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
    

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre', 'estado']

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['fecha', 'total', 'cliente']

class DetalleFacturaForm(forms.ModelForm):
    class Meta:
        model = DetalleFactura
        fields = ['factura', 'producto', 'cantidad', 'precio', 'subtotal']

    
        