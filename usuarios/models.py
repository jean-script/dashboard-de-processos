from django.db import models
from django.contrib.auth.models import User
from Empresas.models import Empresa

# Create your models here.

class Profile(models.Model):

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    foto_perfil = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.usuario)

