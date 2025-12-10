from django.db import models

# Create your models here.

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data = models.DateField()
    autor = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='noticias/', blank=True, null=True)
    categoria = models.CharField(max_length=100)
    
    def __str__(self):
        return self.titulo