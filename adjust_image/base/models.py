from django.db import models

class Imagem(models.Model):
    imagem = models.FileField(upload_to="produtos/", null=True, blank=True)
