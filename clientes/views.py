from django.http import JsonResponse
from rest_framework import viewsets, filters
from clientes.models import Cliente
from .serializer import ClienteSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated 
from django_filters.rest_framework import DjangoFilterBackend

class ClientesViewSet(viewsets.ModelViewSet):

    """ Listando todos os clientes """

    # Definições de busca
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    # Autenticação básica
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # Ordenação das páginas
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
