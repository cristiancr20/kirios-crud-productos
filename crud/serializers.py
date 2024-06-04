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
    marca = MarcaSerializer()
    categoria = CategoriaSerializer()

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precioVenta', 'precioCompra', 'marca', 'categoria', 'stock', 'estado']

    def create(self, validated_data):
        marca_data = validated_data.pop('marca')
        categoria_data = validated_data.pop('categoria')
        marca = Marca.objects.get_or_create(**marca_data)[0]
        categoria = Categoria.objects.get_or_create(**categoria_data)[0]
        producto = Producto.objects.create(marca=marca, categoria=categoria, **validated_data)
        return producto
class DetalleFacturaSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()
    
    class Meta:
        model = DetalleFactura
        fields = ['id', 'factura', 'producto', 'cantidad', 'precio', 'subtotal']

class FacturaSerializer(serializers.ModelSerializer):
    detalles = DetalleFacturaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Factura
        fields = ['id', 'fecha', 'total', 'cliente', 'productos', 'detalles']

    