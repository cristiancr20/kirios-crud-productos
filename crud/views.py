from django.shortcuts import render

from .models import Producto, Marca, Categoria

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    return {
        'productos': productos
        }
