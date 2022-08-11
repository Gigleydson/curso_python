"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá
chamar de qualquer coisa, desde que começe com asterisco.

Exemplo:

*xis

Mas por convenção, utilizamos *args para definí-lo

Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como
entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis.
"""

# Exemplos

# Entendendo o args


def soma_todos_numeros(*args):
    """
    Função que soma todos os número informados.
    :param args: Parâmetro '*args' que possibilita passar quantos números forem necessários para a soma.
    :return: Retorna o total da soma de todos os números informados.
    """
    total = 0
    for numero in args:
        total += numero
    return total


def soma_numeros(*args):
    """
    Função que soma todos os número informados.
    :param args: Parâmetro '*args' que possibilita passar quantos números forem necessários para a soma.
    :return: Retorna o total da soma de todos os números informados.
    """
    return sum(args)  # Utilizando a função 'sum', já que o args é uma tupla


print(soma_numeros())
print(soma_numeros(1))
print(soma_numeros(1, 2))
print(soma_numeros(1, 2, 3))
print(soma_numeros(1, 2, 3, 4))
