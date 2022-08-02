"""
Listas (list)

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e também de podermos colocar em QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:

- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplismente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []

Listas são mutáveis: Ou seja, elas podem mudar constantemente.

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente checar se determinado valor está contido na lista

lista4 = [1, 2, 3, 4, 5, 6, 7]

num = 7

if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')


# Podemos facilmente ordenar uma lista

lista1 = [3, 1, 5, 2, 4]
print(lista1)

lista1.sort()
print(lista1)

lista2 = ['c', 'a', 'd', 'b', 'e']
print(lista2)

lista2.sort()
print(lista2)


# Podemos Facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))


# Adicionar elementos em listas

# Para adicionar elementos em listas, utilizamos a função 'append'
print(lista1)
lista1.append(42)
print(lista1)

# OBS: Com 'append', nós só conseguimos adicionar 1 elemento por vez
# lista1.append(12, 34, 56) # Erro

lista1.append([8, 3, 1])  # Coloca a lista como elemento único (sublista)
print(lista1)

lista1.extend([123, 44, 67])  # Coloca cada elemento da lista como valor adicional à lista
print(lista1)


# Podemos inserir um novo elemento na lista informando a posição do índice
#  OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista.
lista1.insert(2, 'Novo Valor')
print(lista1)


# Podemos facilmente juntar duas listas
lista1 = lista1 + lista2
lista1.extend(lista2)
print(lista1)


# Podemos facilmente inverter uma lista
#  Forma 1
print(lista1)
lista1.reverse()

# Forma 2
print(lista1[::-1])


# Copiar uma lista
lista6 = lista1.copy()
print(lista6)


# Contando os elementos de uma lista
print(len(lista1))


# Podemos remover facilmente o último elemento de uma lista
# OBS: O 'pop' não somente remove o último elemento. Mas também o retorna
print(lista5)
lista5.pop()
print(lista5)


# Podemos remover um elemento pelo índice
# OBS: Os elementos à direita deste índice serão deslocados para a esquerda.
# OBS 2: Se não houver elemento no índice informado, teremos um erro IndexError.
lista5.pop(2)
print(lista5)


# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)


# Podemos facilmente repetir elementos em uma lista.
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)


# Podemos facilmente converter uma string para uma lista.

# Exemplo 1
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão, o 'split' separa os elementos da lista pelo espaço entre elas.

# Exemplo 2
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)


# Convertendo uma lista em string

# Transformando string em lista
lista6 = 'Programação em Python: Essencial'
lista6 = lista6.split()
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: Pega a lista6, coloca um '$' entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)


# Podemos realmente colocar qualquer tipode dado em uma lista, inclusive mistrurando esses dados
lista6 = [1, 2, 34, True, 'Geek', 'd', [1, 2, 3], 4534534534]
print(lista6)
print(type(lista6))


# Iterando sobre listas

# Exemplo 1 - Utilizando 'for'
soma = 0

for elemento in lista4:
    print(elemento)
    soma += elemento

print(soma)


# Exemplo 2 - Utilizando 'while'
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione o produto no carrinho ou digite 'sair', para sair: ")
    produto = input()

    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)


# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)


# Fazemos acesso aos elementos de forma indexada

#           0         1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o índice negativo, pense na lista como um círculo,
# onde o final de um elemento está ligado ao início da lista

print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # verde
# print(cores[-5]) Erro, pois não existe índice -5


# Exemplo de lista com loops

cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1


cores = ['verde', 'amarelo', 'azul', 'branco']

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)


# Encontrar índice de um elemento na lista

# OBS: Em caso de elementos repetidos, retorna o índice do primeiro elemento encontrado.
numeros = [1, 2, 3, 4, 5, 3, 4, 5]
print(numeros.index(3))

# Podemos fazer uma busca dentro de um range, ou seja, qual índice começar a buscar
print(numeros.index(3, 3))  # Buscando a partir do índice 3, ou sejá, o segundo 3

# Podemos fazer uma busca dentro de um range, do ínício ao fim
print(numeros.index(4, 5, 7))  # Buscando o índice do valor 4, entre os índiced 5 e 7

# Outros exemplos
produtos = ['XBOX Series X', 'XBOX Series S', 'Headset XBOX Wireless']
print(produtos.index('XBOX Series S'))


# Revisão de slicing

# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# Trabalhando com slice de lista com o parâmentro 'inicio'

lista = [1, 2, 3, 4]

print(lista[::])  # Pegando todos os elementos
print(lista[1:])  # Iniciando no índice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parâmentro 'fim'
print(lista[:2])  # Começa do 0 e vai até o índice 2 - 1 = (indice 1)
print(lista[:3])  # Começa do 0 e vai até o índice 3 - 1 = (indice 2)
print(lista[1:3])  # Começa do índice 1 e vai até o 3 - 1 = (indice 2)

# Trabalhando com slice de lista com o parâmentto 'passo'
print(lista[1::2])  # Começa em 1, vai até o final, de 2 em 2
print(lista[0::2])  # Começa em 0, vai até o final, de 2 em 2

# Invertendo elementos
nome = 'Gigleydson Dias'
print(nome[::-1])

print(lista[::-1])


# Inventendo valores em uma lista

nomes = ['Gigleydson', 'Dias']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes = ['Izabela', 'Andrade']
nomes.reverse()
print(nomes)


# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # Soma todos os valores da lista
print(max(lista))  # Maior valor da lista
print(min(lista))  # Menor valor da lista
print(len(lista))  # Tamanho da lista


# Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))


# Desempacotamento de listas

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)


# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista,
# mas elas ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra.
# Isso em Python é chamado de Deep Copy (cópia profunda)


# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista
print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista.
# Mas após realizar modificação em uma das litas, essa modificação se refletiu em ambas.
# Isso em Python é chamado de Shallow Copy.

"""


