"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

Formas gerais:

# Forma 1

range(valor_de_parada)

OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

# Exemplo Forma 1
for num in range(11):
    print(num)


# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (início definido pelo usuário, e passo de 1 em 1)

# Exemplo Forma 2
for num in range(1, 11):
    print(num)


# Forma 3

range(valor_de_início, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (início definido pelo usuário, e passo definido pelo usuário)

# Exemplo Forma 3
for num in range(5, 55, 5):
    print(num)


# Forma 4 (Inversa)

range(valor_inicial, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (valor_inicial definido pelo usuário, e passo definido pelo usuário)

# Exemplo Forma 4
for num in range(10, -1, -1):
    print(num)

"""

# Exemplo de um range sendo transformado em uma lista
lista = list(range(10))
print(lista)









