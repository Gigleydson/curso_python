"""
Map

Com map, fazemos mapeamento de valors para função.
"""

import math


def area(r):
    """Calcula a área de um círculo com raia 'r'."""
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))


raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Forma 2 - Map

# Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável. Retorna um Map Object

areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))
