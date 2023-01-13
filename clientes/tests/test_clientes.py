from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from clientes.models import Cliente
from django.urls import reverse
from rest_framework import status



class ClientesTestCase(APITestCase):
    
    def setUp(self):

        self.list_url_clientes = reverse('Clientes-list')
        self.user = User.objects.create_user('teste', password='teste')

        self.cliente_valido = Cliente.objects.create(nome="joao", cpf="58972443085", data_nascimento="1990-01-01")

        

    def test_requisicao_get_para_listar_todos_os_clientes_salvos(self):
        """ Teste que verifica a requisição Get para listar todos os clientes cadastrados. """
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url_clientes)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_requisicao_post_para_criar_cliente_com_cpf_valido(self):
        """ Teste que verifica a requisição post para criar cliente com cpf válido. """
        self.client.force_authenticate(self.user)
        data =  {
            'nome': 'nome_teste_valido',
            'cpf': '224.771.260-67',
            'data_nascimento': '1990-01-01'
        }
        response = self.client.post(self.list_url_clientes, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_post_para_criar_cliente_com_cpf_invalido(self):
        """ Teste que verifica a requisição post para criar cliente com cpf inválido. """
        self.client.force_authenticate(self.user)
        data =  {
            'nome': 'nome_teste_invalido',
            'cpf': '21345678901',
            'data_nascimento': '1990-06-02'
        }
        response = self.client.post(self.list_url_clientes, data=data)

        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_requisicao_get_para_buscar_cliente_por_cpf(self):
        """ Teste que verifica a requisição get para buscar um cliente por cpf"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url_clientes, kwargs={'cpf':'22477126067'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['nome'], 'joao')
  
        