from django.db import models
import string
import random

# Create your models here.


class ArchivoUrl(models.Model):
    """
    Guarda un registro por cada archivo con url's que se envia al servicio web.
    Agrupa las url's del archivo para poder descargar la version corta
    """

    nombre = models.CharField(max_length=250, unique=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.nombre


class Url(models.Model):
    """
    Guarda URLs completas u originales y genera un codigo para cada nueva URL 
    con una longitud maxima de 6 caracteres, comprendiendo de letras 
    mayusculas y minusculas asi como numeros.

    """
    original = models.URLField(max_length=2000, unique=True)
    codigo = models.CharField(max_length=6, unique=True)
    archivo = models.ForeignKey(ArchivoUrl, null=True, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.original

    def save(self, *args, **kwargs):
        # Al crear el registro, se genera un valor aleatorio para el atributo
        # 'codigo'
        if not self.id:
            opciones = ( string.ascii_uppercase 
                        + string.ascii_lowercase 
                        + string.digits )
            self.codigo = ''.join(random.choices(opciones, k=6))
        super().save(*args, **kwargs)


