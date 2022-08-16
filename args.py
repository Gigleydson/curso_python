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


# Exemplos

# Entendendo o args


def soma_todos_numeros(*args):

    Função que soma todos os número informados.
    :param 'args': Parâmetro '*args' que possibilita passar quantos números forem necessários para a soma.
    :return: Retorna o total da soma de todos os números informados.

    total = 0
    for numero in args:
        total += numero
    return total


def soma_numeros(*args):

    Função que soma todos os número informados.
    :param 'args': Parâmetro '*args' que possibilita passar quantos números forem necessários para a soma.
    :return: Retorna o total da soma de todos os números informados.

    return sum(args)  # Utilizando a função 'sum', já que o args é uma tupla


print(soma_numeros())
print(soma_numeros(1))
print(soma_numeros(1, 2))
print(soma_numeros(1, 2, 3))
print(soma_numeros(1, 2, 3, 4))


# Outro exemplo de utilização do #arges


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Você não é um Geek!'


print(verifica_info())
print(verifica_info(1, True, 'University', 3, 'Geek'))
print(verifica_info(1, 'University', 3.145))
"""


def soma_numeros(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5]

# Desempacotador

print(soma_numeros(*numeros))

# OBS: O asterisco serve para que informamos ao Python que estamos
# passando como argumento uma coleção de dados.
# Desta forma, ele saberá que precisamos antes desempacotar estes dados.
