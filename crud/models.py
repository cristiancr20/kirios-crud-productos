# models.py
from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=1, default='V')

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.estado = True
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precioVenta = models.DecimalField(max_digits=10, decimal_places=2)
    precioCompra = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50, default='True')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='productos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre
