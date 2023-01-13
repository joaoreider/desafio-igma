<h1 align="center"> API de cadastro de clientes | Desafio técnico IGMA</h1>

<p style='text-align: justify;'> 
Uma API para cadastrar clientes com validação de CPF antes de salvar no banco de dados.
</p>


## :hammer: Endpoints atuais


###  GET `/clientes/`

. Lista todos os clientes cadastrados no banco de dados.

- Response:
  ```python
  {
  "count": int,
  "next": str # url da próxima página
  "previous": str # url da página anterior
  "results": 
    {
      "id": int,
      "nome": str,
      "cpf": str,
      "data_nascimento": str 
    }
  }
  ```

Foi feita uma configuração de paginação de 3 clientes por página. Você pode acessar a página passando o parâmetro _page_, exemplo: "http://127.0.0.1:8000/clientes/?page=2" acessa a segunda página de clientes.

###  POST `/clientes/`

. Cadastra um cliente no banco de dados

- Enviar dados (obrigatório):
  ```python
  
  {

      "nome": str,
      "cpf": str,
      "data_nascimento": str ('yyyy-mm-dd')
    }
  ```

O CPF pode ser passado com máscara ou sem máscara, mas é importante que seja um cpf válido. Um retorno http status 422 significa que você passou um cpf inválido.

###  GET `/clientes/?search=<cpf>`

. Busca um cliente pelo cpf passado como parâmetro

- Response:
  ```python
    {
      "id": int,
      "nome": str,
      "cpf": str,
      "data_nascimento": str 
    }

  ```


## ✔️ Técnicas e tecnologias utilizadas


- [``Django Rest Framework``](https://wwwdjango-rest-framework.org/)
- [``Expressões regulares``](https://docs.python.org/3/library/re.html)
- [``Swagger``](https://swagger.io/)
- [``Framework Django``](https://docs.djangoproject.com/en/4.1/)
- [``Linguagem Python``](https://docs.python.org/3/)
- ``Ambientes virtuais``
- ``Paradigma de orientação a objetos``



## 🛠️ Instalação


1. Clone o repositório para sua máquina:


```
$ git clone https://github.com/joaoreider/desafio-igma/
```

2. Crie um ambiente virtual e ative-o:

```
python -m venv venv

Linux/macOS
source venv/bin/activate

windows
venv/Scripts/Activate

```

3. Entre na pasta desafio-igma e instale as dependências:
```
Linux/macOS:
$ pip3 install -r requirements.txt

Windows:
pip install -r requirements.txt
```
4. Faça as migrações para o banco de dados:
```
python manage.py makemigrations
python manage.py migrate

```
5. Inicie o servidor local:

```
python manage.py runserver
```

6. Acesse a página da API em http://127.0.0.1:8000/
*Utilize as credenciais:
username = admin
senha = admin*


## :computer: Testes

Para rodar os testes, execute o comando:
```
python manage.py test
```

:point_down: Acesse meu perfil no Linkedin 
<div> 
 <a href="https://www.linkedin.com/in/jo%C3%A3o-paulo-2345b3170/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>



</div>
