# mi_aplicacion/api_views.py
from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import Producto, Categoria, Marca, Factura, DetalleFactura
from .serializers import ProductoSerializer, CategoriaSerializer, MarcaSerializer, FacturaSerializer, DetalleFacturaSerializer
from rest_framework.views import APIView
from rest_framework import status

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class DetalleFacturaViewSet(viewsets.ModelViewSet):
    queryset = DetalleFactura.objects.all()
    serializer_class = DetalleFacturaSerializer



class BuscarProductos(APIView):
    def get(self, request):
        termino = request.query_params.get('termino', None)
        if termino:
            productos = Producto.objects.filter(nombre__icontains=termino)
            serializer = ProductoSerializer(productos, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Se requiere el parámetro 'termino' en la consulta GET"}, status=status.HTTP_400_BAD_REQUEST)

class GuardarFactura(APIView):
    def post(self, request):
        serializer = FacturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
