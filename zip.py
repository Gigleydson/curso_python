"""
Zip

zip() -> Cria um iterável (Zip Object) que agrega elemento de cada um dos iteráveis passados como entrada em pares.

Exemplos

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2, 'abc')

print(zip1)

print(list(zip1))

zip1 = zip(lista1, lista2, 'abc')
print(tuple(zip1))

zip1 = zip(lista1, lista2, 'abc')
print(set(zip1))

zip1 = zip(lista1, lista2)
print(dict(zip1))

# OBS: O zip() utiliza como parâmetro o menor tamanho em iterável. Isso Significa que se estiver trabalhando
com iteráveis de tamanhos diferentes, irá parar quando os elementos do menor iterável acabar.

lista3 = [7, 8, 9, 10]
zip1 = zip(lista1, lista2, lista3)
print(list(zip1))
"""
