"""
Só exercícios
"""

valores = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}

nota = input('Digite uma nota de 0 a 10: ')

while nota not in valores:
    print('Valor inválido!')
    nota = input('Digite uma nota de 0 a 10: ')

print(f'A nota atribuída foi {nota}')
