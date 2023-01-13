from rest_framework import serializers, status
from rest_framework.exceptions import APIException
from clientes.models import Cliente
from clientes.validators import *
from re import sub

class CPFInvalido(APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = 'CPF inválido.'

class ClienteSerializer(serializers.ModelSerializer):
    """Exibindo todos os clientes"""
    class Meta:
        model = Cliente 
        fields = ['id', 'nome', 'cpf', 'data_nascimento']
    
    def validate_cpf(self, data):
       
        cpf = sub('[^0-9]', '', data)
        
        if not cpf_valido(cpf):
            raise CPFInvalido({'cpf':"CPF inválido"})

        return cpf 
          