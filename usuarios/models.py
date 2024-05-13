from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    choices_permissao = (('P', 'PontoColeta'),
                     ('A', 'Administrador'),
                     ('C', 'Catador'))
    permissao = models.CharField(max_length=1, choices=choices_permissao)
