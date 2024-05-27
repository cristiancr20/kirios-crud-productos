from django.db import models


# Create your models here.
#modelo de productos de locales 

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    precioVenta = models.DecimalField(max_digits=10, decimal_places=2)
    precioCompra = models.DecimalField(max_digits=10, decimal_places=2)
"""     marca = models.ForeignKey('Marca', on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE) """




    
class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    producto = models.ManyToOneRel(Producto, related_name='marcas')


    
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    producto = models.ManyToOneRel(Producto, related_name='categorias')



    
