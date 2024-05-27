from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    path('', views.index, name='index'),
    
    #PRODUCTOS
    path('producto/crear/', views.crear, name='crear'),
    path('producto/editar/<int:id>/', views.editar, name='editar'),
    path('producto/eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('producto/ver/', views.ver, name='ver'),

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
    
   
]