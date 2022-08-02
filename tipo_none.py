"""
Tipo None

O tipo de dado None em Python representa o tipo sem tipo, ou poderia ser cinheido também como tipo vazio,
porém, falar que é um tipo sem tipo é mais apropriado.

OBS: O tipo None é SEMPRE especificado com a primeira letra maiúscula.

Certo: None
Errado: none

Quando utilizarmos?

- Podemos utilizar None quando queremos criar uma variável e inicializa-lá com um tipo sem tipo,
antes de recebermos um valor final.

OBS: O tipo None em Python é SEMPRE considerado como False
"""

numeros = None

print(numeros)
print(type(numeros))

numeros = 1, 2, 3

print(numeros)
print(type(numeros))
