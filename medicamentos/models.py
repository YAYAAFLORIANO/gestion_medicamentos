from django.db import models

class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    concentracion = models.CharField(max_length=50)
    presentacion = models.CharField(max_length=50)
    stock_minimo = models.IntegerField()

    def __str__(self):
        return self.nombre