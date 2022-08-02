"""
Funções com retorno

OBS: Em Python, quando uma função mão retorna nenhum valor, o retorno é 'None'

OBS: Funções Python que retornam valores, devem retornar estes valores com a palavra reservada return

OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma função.
Podemos passar a execução da função para outras funções.


# Exemplo de função com retorno


def quadrado_de_7():
    return 7 * 7


# Criamos uma variável para receber o retorno da função
ret = quadrado_de_7()
print(f'Retorno {ret}')

# Podemos passar a vaiável diretamente no print.
print(f'Retorno: {quadrado_de_7()}')


# Refatorando a primeira função

def diz_oi():
    return 'Oi '


alguem = 'Pedro'

print(f'{diz_oi() + alguem}!')

OBS: A vantagem de usar return para imprimir a função e não imprimir diretamente dentro dela
é que você pode utilizar o dado que a função está gerando, como na linha de código acima.

OBS: Sobre a palavra reservada 'return'

1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;

# Exemplo 1 - Ela finaliza a função, ou seja, ela sai da execução da função;
def diz_oi():
    print('Estou sendo impresso porque estou antes do return')
    return 'Oi!'
    print('Não estou sendo impresso porque estou depois do return')


print(diz_oi())


# Exemplo 2 - Podemos ter, em uma função, diferentes returns;
def nova_funcao():
    variavel = True
    if variavel:
        return 'Verdadeiro'
    elif variavel is None:
        return 0
    return 'Falso'


print(nova_funcao())


# Exemplo 3 - Podemos em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;
def outra_funcao():
    return 2, 3, 4, 5


# num1, num2, num3, num4 = outra_funcao()
# print(num1, num2, num3, num4)

print(outra_funcao())
print(type(outra_funcao()))


# Vamos criar uma função para jogar a moeda

# Importando a função random da biblioteca random
from random import random


def jogar_moeda():
    # A fução random gera um número pseudo-randômico entre 0 e 1
    # valor = random()
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(jogar_moeda())
"""

