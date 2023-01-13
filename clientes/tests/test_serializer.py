from django.test import TestCase
from clientes.models import Cliente
from clientes.serializer import ClienteSerializer

class CLienteSerializerTestCase(TestCase):

    def setUp(self):

        self.cliente = Cliente(
            nome = 'Joao',
            cpf = '550.889.140-40',
            data_nascimento = '1999-08-14'
        )

        self.serializer = ClienteSerializer(instance=self.cliente)
    
    def test_verifica_campos_serializados(self):

        """ Test que verifica os campos que estão sendo serializados """
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'nome', 'cpf', 'data_nascimento']))

    def test_verifica_conteudo_dos_campos_serializados(self):

        """ Test que verifica o conteúdo dos campos que estão sendo serializados """
        data = self.serializer.data
        self.assertEqual(data['nome'], self.cliente.nome)
        self.assertEqual(data['cpf'], self.cliente.cpf)
        self.assertEqual(data['data_nascimento'], self.cliente.data_nascimento)