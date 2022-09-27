"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.

# Exemplo all()

print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros? False
print(all([1, 2, 3, 4]))  # Todos os números são verdadeiros? True
print(all([]))  # Todos os números são verdadeiros? True
print(all((1, 2, 3, 4)))  # Todos os números são verdadeiros? True
print(all({1, 2, 3, 4}))  # Todos os números são verdadeiros? True
print(all('Geek'))  # Todos os números são verdadeiros? True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes]))

# OBS: Um iterável vazio convertido em boolean é False, mas o all() entende como True
print(all(letra for letra in 'eio' if letra in 'aeiou'))

print(all([numero for numero in [2, 4, 6, 8, 10] if numero % 2 == 0]))
print(all([numero % 2 == 0 for numero in [2, 4, 6, 8, 10]]))


any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False.
"""

print(any([0, 1, 2, 3, 4]))  # True
print(any([0, False, '', [], {}, ()]))  # False

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Neto']
print(any([nome[0] == 'C' for nome in nomes]))  # True

print(any([numero for numero in [2, 4, 6, 8, 10] if numero % 2 == 0]))  # True
print(any([numero for numero in [2, 4, 6, 8, 10] if numero % 2 == 1]))  # False

