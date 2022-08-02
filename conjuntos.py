"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos da Matemática.

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:

- Sets (Conjuntos) não possuem valores duplicados;
- Sets (Conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles.
Quando não precisamos nos preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (Set) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;


# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos.

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar error e não fará parte do conjunto.

# Forma 2- Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))


# Podemos verificar se determinado elemento está contido no conjunto

numero = int(input('Digite o número que deseja buscar: '))

if numero in s:
    print(f'Número {numero} encontrado!')
else:
    print(f'Número {numero} não encontrado!')


# Importante lembrar que, além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionários não aceitam valores duplicados, então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')


# Assim como qualquer outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente

for valor in s:
    print(valor)


# Usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
# informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Natal', 'Recife', 'Fortaleza', 'Natal', 'João Pessoa', 'Recife', 'Salvador']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.

# O que você faria? Faria um loop na lista...?

# Podemos utilizar o set para isso:

print(len(set(cidades)))


# Adicionando elementos em um conjunto

s = {1, 2, 3}
print(s)

s.add(4)
s.add(4)  # Duplicidade não gera erro. Simplismente é ignorado e não adicionado.
print(s)


# Remover elementos em um conjunto

s = {1, 2, 3}
print(s)

# Forma 1
s.remove(3)  # Não é índice! Informamos o valor a ser removido.
print(s)

# OBS: Caso o valor não seja encontrado será gerado o erro KeyError

# Forma 2
s.discard(2)
print(s)

# OBS: Se o valor não for encontrato, nenhum erro é gerado.


# Copiando um conjunto para outro

s = {1, 2, 3}
print(s)

# Forma 1 - Deep Copy
novo = s.copy()
novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow Copy
novo = s
novo.add(4)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto
s.clear()
print(s)


# Métodos Matemáticos de Conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um
# contendo estudantes do curso de Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python também estudam Java.

# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)
# {'Gustavo', 'Ellen', 'Fernando', 'Marcos', 'Julia', 'Patricia', 'Guilherme', 'Ana', 'Pedro'}

# Forma 2 - Utilizando o caractere pipe '|'
unicos2 = estudantes_python | estudantes_java
print(unicos2)
# {'Gustavo', 'Ellen', 'Fernando', 'Marcos', 'Julia', 'Patricia', 'Guilherme', 'Ana', 'Pedro'}


# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)
# {'Patricia', 'Julia'}

# Forma 2 - Utilizando o '&'

ambos2 = estudantes_python & estudantes_java
print(ambos2)
# {'Julia', 'Patricia'}


# Gerar um conjunto de estudantes de um curso que não estão no outro

so_python = estudantes_python.difference(estudantes_java)
print(so_python)
# {'Pedro', 'Ellen', 'Guilherme', 'Marcos'}

so_java = estudantes_java.difference(estudantes_python)
print(so_java)
# {'Fernando', 'Ana', 'Gustavo'}
"""

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
