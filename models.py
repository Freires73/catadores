from django.db import models

    
class Pontocoletas(models.Model):
    nome = models.CharField(max_length=40)
    endereco = models.CharField(max_length=40)
    telefone = models.CharField(max_length=40)
    bairro = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.nome
