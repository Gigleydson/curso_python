"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em Listas.
O sort() só funciona em listas. Modificando a lista original.

Podemos utilizar o sorted() com qualquer iterável. Ele gera uma nova lista, sem modificar a lista original.

Como o próprio nome diz, sorted() serve para ordenar.

OBS: O sorted sempre retorna uma Lista com os elementos do iterável ordenados.

# Exemplo

numeros = {6, 1, 8, 4}
print(numeros)
print(sorted(numeros))  # Ordena do menor para o maior
print(numeros)


numeros = [6, 1, 8, 4]
print(numeros)

print(set(sorted(numeros)))  # Podemos tranformar a lista em outros tipos de iteráveis. Nesse caso Set.

# Adicionando parâmetros ao sorted()
print(sorted(numeros, reverse=True))  # Ordena do maior para o menor


usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolo', 'Eu adoro pizza']},
    {'username': 'andre', 'tweets': ['Hoje é meu aniversário']},
    {'username': 'jorge', 'tweets': []},
    {'username': 'samuel', 'tweets': []},
    {'username': 'felipe', 'tweets': ['Estou de férias!', 'Comprei um tênis novo']},
    {'username': 'marcos', 'tweets': []}
]

print(usuarios)

# Ordenando por username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando por número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))
"""

musicas = [
    {'titulo': 'In the end', 'tocou': 10},
    {'titulo': 'Welcome to the jangle', 'tocou': 2},
    {'titulo': 'Last resort', 'tocou': 5},
    {'titulo': 'American idiot', 'tocou': 7}
]

print(musicas)

# Odenando da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Odenando da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
