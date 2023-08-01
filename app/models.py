from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    editorial = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo