from django.db import models
from django.conf import settings

class Cliente(models.Model):
    
    nome = models.CharField(max_length=127)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField() 

    def __str__(self):
        return self.nome
