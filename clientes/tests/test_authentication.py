
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.list_url_clientes = reverse('Clientes-list')
        self.user = User.objects.create_user('teste', password='teste')

    def test_autenticacao_de_usuario_valido(self):
        """ Teste que verifica se um usuário com as credenciais corretas consegue acessar a API"""

        user = authenticate(username='teste', password='teste')

        self.assertTrue((user is not None) and user.is_authenticated)
    
    def test_requisicao_get_sem_estar_autenticado(self):
        """ Teste para verificar uma requisição Get não autorizada"""
        response = self.client.get(self.list_url_clientes)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED) 

    def test_autenticacao_de_usuario_com_username_incorreto(self):
        """ Teste que verifica se um usuário com username incorreto consegue acessar a API"""

        user = authenticate(username='teste_errado', password='teste')

        self.assertFalse((user is not None) and user.is_authenticated)
    
    def test_autenticacao_de_usuario_com_senha_incorreta(self):
        """ Teste que verifica se um usuário com senha incorreta consegue acessar a API"""

        user = authenticate(username='teste', password='teste_errado')

        self.assertFalse((user is not None) and user.is_authenticated)
    

    def test_requisicao_get_de_usuario_autenticado(self):
        """ Teste para verificar uma requisição Get autorizada"""

        self.client.force_authenticate(self.user)

        response = self.client.get(self.list_url_clientes)

        self.assertEqual(response.status_code, status.HTTP_200_OK) 
