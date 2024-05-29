from django.urls import path
from . import views
from .views import buscar_productos, agregar_producto, actualizar_cantidad, guardar_factura

app_name = 'crud'

urlpatterns = [
    path('', views.index, name='index'),
    
    #PRODUCTOS
    path('producto/crear/', views.crear, name='crearProducto'),
    path('producto/editar/<int:id>/', views.editar, name='editarProducto'),
    path('producto/eliminar/<int:id>/', views.eliminar, name='eliminarProducto'),
    path('producto/ver/', views.ver, name='verProducto'),

    #CATEGORIAS
    path('categoria/crear/', views.crearCategoria, name='crearCategoria'),
    path('categoria/editar/<int:id>/', views.editarCategoria, name='editarCategoria'),
    path('categoria/eliminar/<int:id>/', views.eliminarCategoria, name='eliminarCategoria'),
    path('categoria/ver/', views.verCategoria, name='verCategoria'),

    #MARCAS
    path('marca/crear/', views.crearMarca, name='crearMarca'),
    path('marca/editar/<int:id>/', views.editarMarca, name='editarMarca'),
    path('marca/eliminar/<int:id>/', views.eliminarMarca, name='eliminarMarca'),
    path('marca/ver/', views.verMarca, name='verMarca'),

    #FACTURAS

    #BUSCAR
    path('buscar/', buscar_productos, name='buscar_productos'),
    path('agregar/<int:producto_id>/', agregar_producto, name='agregar_producto'),
    path('actualizar/<int:producto_id>/', actualizar_cantidad, name='actualizar_cantidad'),
    path('guardar/', guardar_factura, name='guardar_factura'),
    path('ver_facturas/', views.ver_facturas, name='ver_facturas'),
    path('ver_detalle_factura/<int:factura_id>/', views.ver_detalle_factura, name='ver_detalle_factura'),
    path('eliminar_factura/<int:factura_id>/', views.eliminar_factura, name='eliminar_factura'),

]