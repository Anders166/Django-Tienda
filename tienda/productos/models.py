from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name='productos'
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
