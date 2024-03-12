from django.db import models

class Pokemon(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
