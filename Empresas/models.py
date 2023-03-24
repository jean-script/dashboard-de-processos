from django.db import models

# Create your models here.

class Empresa(models.Model):
    
    nome_empresa = models.CharField(max_length=200)
    foto_empresa = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)

    def __str__(self):
        return self.nome_empresa
    