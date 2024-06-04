# mi_aplicacion/api_urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .api_views import ProductoViewSet, CategoriaViewSet, MarcaViewSet, FacturaViewSet, DetalleFacturaViewSet, BuscarProductos, GuardarFactura

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'marcas', MarcaViewSet)
router.register(r'facturas', FacturaViewSet)
router.register(r'detalle_facturas', DetalleFacturaViewSet)

# Definir manualmente la ruta para la vista BuscarProductos
urlpatterns = [
    # Rutas de los viewsets
    path('productos/buscar/', BuscarProductos.as_view(), name='buscar_productos'),
    path('facturas/guardar/', GuardarFactura.as_view(), name='guardar_factura'),


]

urlpatterns += router.urls
