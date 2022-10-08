"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.

# Exemplo

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))  # 129

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))  # 129

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))  # 129

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario))  # 'f' -> Passa Keys por padrão

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.values()))  # 129


# Faça um programa que receba dois valores do usuário e mostre o maior:

valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))

print(f'O maior valor é', max(valor1, valor2))

print(max('a', 'ab', 'abc'))

print(max('a', 'b', 'c', 'd'))

print(max('Geek University'))

print(max('gigleydson'))


min() -> Retorna o menor valor em um iterável ou o menor de 2 ou mais elementos.

# Exemplo

lista = [1, 8, 4, 99, 34, 129]
print(min(lista))  # 1


lista = [1, 8, 4, 99, 34, 129]
print(min(lista))  # 1

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla))  # 1

conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto))  #

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario))  # 'a' -> Passa Keys por padrão

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario.values()))  # 1


# Faça um programa que receba dois valores do usuário e mostre o menor:

valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))

print(f'O menor valor é', min(valor1, valor2))

print(min('a', 'ab', 'abc'))

print(min('a', 'b', 'c', 'd'))

print(min('gigleydson'))


# Outros Exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(max(nomes))  # Tim
print(min(nomes))  # Arya

print(max(nomes, key=lambda nome: len(nome)))  # Ollivander
print(min(nomes, key=lambda nome: len(nome)))  # Tim
"""

musicas = [
    {'titulo': 'In the end', 'tocou': 10},
    {'titulo': 'Welcome to the jangle', 'tocou': 2},
    {'titulo': 'Last resort', 'tocou': 5},
    {'titulo': 'American idiot', 'tocou': 7}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))


# DESAFIO! Imprima somente o título da música mais e menos tocada:
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

print('')

# DESAFIO! Como encontrar a música mais tocada e a menos tocada sem usar max(), min() e lambda?

maximo = 0
for musica in musicas:
    if musica['tocou'] > maximo:
        maximo = musica['tocou']

for musica in musicas:
    if musica['tocou'] == maximo:
        print(musica['titulo'])


minimo = 99999
for musica in musicas:
    if musica['tocou'] < minimo:
        minimo = musica['tocou']

for musica in musicas:
    if musica['tocou'] == minimo:
        print(musica)
