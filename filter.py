"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.


# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f'Média: {media}')

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo uma função e um iterável.

res = filter(lambda valor: valor > media, dados)
print(list(res))

# OBS: Assim como a função map(), após serem utilizados os dados de filter() eles são excluídos da memória.

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)

# res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(lambda pais: pais != '', paises)
res = filter(None, paises)

print(list(res))
"""

# Exemplo mais complexo

usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolo', 'Eu adoro pizza']},
    {'username': 'andre', 'tweets': ['Hoje é meu aniversário']},
    {'username': 'jorge', 'tweets': []},
    {'username': 'samuel', 'tweets': []},
    {'username': 'felipe', 'tweets': ['Estou de férias!', 'Comprei um tênis novo']},
    {'username': 'marcos', 'tweets': []}
]

print(usuarios)


# Filtrar os usuários que estão ativos no Twitter

# Forma 1
# inavitos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

# Forma 2
inavitos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inavitos)