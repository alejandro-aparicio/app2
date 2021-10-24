from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre_medicamento = models.CharField(max_length=200)
    descripción = models.TextField()
    imagen = models.ImageField(verbose_name="Imagen", upload_to="proyectos", default="")



    def __str__(self):
        return self.nombre_medicamento
