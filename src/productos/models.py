from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length= 30)
    marca = models.CharField(max_length= 30)
    precio = models.FloatField()
    fecha_vencimiento = models.DateField(blank=True, null=True)
    stock = models.IntegerField(default=50)

    def __str__(self):
        return f"{self.nombre} - {self.marca}" 
