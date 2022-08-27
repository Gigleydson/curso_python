"""
Listas Aninhadas (Nested Lists)

- Algumas linguagens de programação (C/Java) possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes):


Em Python nós temos as Listas

list = [1, 'b', 3.234, True, 5]
"""

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3
print(listas)
print(type(listas))

# Como fazer para acessar os dados?
print(listas[0][1])  # 2
print(listas[2][1])  # 8
