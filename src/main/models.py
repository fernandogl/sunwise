from django.db import models
import string
import random

# Create your models here.


class Url( models.Model ):
    """
    Guarda URLs completas u originales y genera un codigo para cada nueva URL 
    con una longitud maxima de 6 caracteres, comprendiendo de letras 
    mayusculas y minusculas asi como numeros.

    """
    original = models.URLField(max_length=2000, unique=True)
    codigo = models.CharField(max_length=6, unique=True)
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