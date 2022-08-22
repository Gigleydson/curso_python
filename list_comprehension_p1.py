"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável.


# Sintax da List Comprehension

[ dado for dado in iterável ]


# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10


res = [numero / 2 for numero in numeros]
print(res)


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(res)


# List Comprehension versos Loop

# Loop
numeros_dobrados = []

for numero in [1, 2, 3, 4, 5]:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)


# List Comprehension
print([numero * 2 for numero in [1, 2, 3, 4, 5]])

"""


# Outros exemplos

# 1
nome = 'Gigleydson Dias'
print([letra.upper() for letra in nome])

# 2
amigos = ['adail', 'bruno', 'hudson', 'almeida', 'augusto']
print([amigo.title() for amigo in amigos])
