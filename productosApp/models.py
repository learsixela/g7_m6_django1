from django.db import models

# Create your models(class)(tabla) here.
class Producto(models.Model):
    #nombre_atributo = tipo_de_dato
    nombre = models.CharField(max_length=40)#varchar
    descripcion = models.TextField()
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #deleted_at

    def __str__(self) -> str:
        return f"Objeto Producto: {self.id} - {self.nombre} "
