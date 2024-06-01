from rest_framework import serializers
from .models import Factura, DetalleFactura, Producto, Categoria, Marca


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'nombre']

class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    marca = MarcaSerializer()

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precioVenta', 'precioCompra', 'marca', 'categoria', 'stock', 'estado']

class DetalleFacturaSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()
    
    class Meta:
        model = DetalleFactura
        fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
    detalles = DetalleFacturaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Factura
        fields = '__all__'
