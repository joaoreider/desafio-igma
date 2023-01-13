from django.contrib import admin
from clientes.models import Cliente


class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', )
    list_per_page = 20
    ordering=('nome', ) 

admin.site.register(Cliente, Clientes)