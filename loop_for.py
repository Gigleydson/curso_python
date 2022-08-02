"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas.

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.

Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7. 9]
- Range
    numeros = range(1, 10) -> (valor_inicial, valor_final) Mas o último valor não é impresso.

Enumerate

((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k')...)

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um 'underline'( _ )

Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""

nome = 'Gigleydson Dias'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra, end='')  # O end='' é utilizado para não pular uma linha na impressão da próxima letra.

print('\n')

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

print('\n')

# Exemplo de for 3 (Iterando sobre uma range)
for numero in numeros:
    print(numero)

print('\n')

qtd = int(input('Digite a quantidade de vezes que esse loop tem que rodar: '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Digite o {n}/{qtd} valor: '))
    soma = soma + num

print(f'A soma é {soma}, \n')


"""
Emoji carinha apaixonada
Original: U+1F60D
Modificado: U0001F60D
"""

emoji = '\U0001F60D'  # O '\' serve para ignorar o que vem depois.

for num in range(1, 11):
    print(emoji * num)


