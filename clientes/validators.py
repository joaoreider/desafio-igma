

# Função para validação de CPF
def cpf_valido(cpf):

    """
    O algoritmo de validação do CPF calcula o primeiro dígito verificador
    a partir dos 9 primeiros dígitos do CPF, e, em seguida, calcula o segundo
    dígito verificador a partir dos 9 (nove) primeiros dígitos do CPF,
    mais o primeiro dígito, obtido na primeira parte.
    """


    # Separa os primeiros nove dígitos do cpf
    cpf_nove_digitos = cpf[:-2]

    soma_digito_1, soma_digito_2 = 0, 0

    # Realiza a soma para calcular os dígitos 
    for index, valor in enumerate(cpf_nove_digitos, -10):

        soma_digito_1 += abs(index) * int(valor)
        soma_digito_2 += abs(index-1) * int(valor)

    # Cálculo do primeiro dígito
    resto_digito_1 = soma_digito_1 % 11
    digito_1 = 0 if (resto_digito_1 < 2) else 11-resto_digito_1

    # Cálculo do segundo dígito (atualiza a soma com o primeiro dídigo calculado)
    soma_digito_2 = soma_digito_2 + (digito_1 * 2)
    resto_digito_2 = soma_digito_2 % 11
    digito_2 = 0 if (resto_digito_2 < 2) else 11-resto_digito_2

    # cpf válido com base nos nove primeiros dígitos fornecidos
    cpf_valido = cpf_nove_digitos + str(digito_1) + str(digito_2)

    return cpf_valido == cpf 

