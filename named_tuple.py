"""
Módulo Collections - Named Tuple

# Recap tupla
tupla = (1, 2, 3)
print(tupla[1])

Named Tupla -> São tuplas, diferenciadas, onde especificamos um nome para a mesma e também parâmetros.
"""

# Importando
from collections import namedtuple

# Precisamos definir o nome e parâmetro.

# Forma 1 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando
jake = cachorro(idade=10, raca='German Sherphed', nome='Jake')
print(jake)

# Acessando os dados

# Forma 1
print(jake[0])  # idade
print(jake[1])  # raça
print(jake[2])  # nome

# Forma 2
print(jake.idade)  # idade
print(jake.raca)  # raça
print(jake.nome)  # nome
