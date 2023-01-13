import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random


class Cliente():

    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
    

def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        cpf = cpf.generate()
        
        dt_nascimento = '1999-08-14'
        
        p = Cliente(nome=nome, cpf=cpf, data_nascimento= dt_nascimento)
        p.save()

criando_pessoas(50)
print('sucesso')