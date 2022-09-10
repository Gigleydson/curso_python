"""
Utilizando Lambdas

Cconhecidas por Expressões Lambdas ou simplismente Lambdas, são funções sem nome,
ou seja, funções anônimas.

# Função em Python
def funcao(x):
    return 3 * x + 1

print(funcao(4))
print(funcao(7))


# Expressão Lambda
lambda x: 3 * x + 1

# E como utilizar a expressão lambda?
calculo = lambda x: 3 * x + 1

print(calculo(4))
print(calculo(7))


# Podemos ter expressões lambdas com múltiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

# strip() - Retira os espações de uma palavra entre aspas, do início e do fim das aspas.

print(nome_completo(' gigleydson ', ' DIAS'))


# Em funções Python podemos ter nenhuma ou várias entradas. Em Lambdas também.

amar = lambda: 'Como não amar Python?'

uma = lambda x: 3 * x + 4

duas = lambda x, y: (x * y) ** 2

tres = lambda x, y, z: x * y / z

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(2, 8, 4))

# OBS: Se passarmos mais argumentos do que parâmetros esperados teremos TypeError


# Outro exemplo

nomes = ['Gigleydson Dias', 'Bruno Oliveira', 'Izabela Andrade', 'José H. André', 'Amanda Ferreira Costa',
         'J. S. Alencar']

print(nomes)

nomes.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(nomes)
"""

# Função Quadrática
# f(x) = a * x ** 2 + b * x + c


# Definindo a função

def gerador_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c


funcao = gerador_funcao_quadratica(2, 3, -5)

print(funcao(0))
print(funcao(1))
print(funcao(2))

print(gerador_funcao_quadratica(3, 0, 1)(2))
