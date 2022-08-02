"""
Recebendo dados do usuário
"""
# Entrada de dados
# print("Qual é o seu nome? ")
# nome = input()

nome = input('Qual o seu nome? ').title()

# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a) %s' % nome.title())

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a) {0}' .format(nome.title()))

# Exemplo de print 'mais atual' acima de 3.7
print(f'Seja bem-vindo(a) {nome}')

# print("Qual a sua idade? ")
# idade = input()

idade = int(input('Qual a sua idade? '))

# Processamento

# Saída de dados

# Exemplo de print 'antigo' 2.x
# print('%s tem %s anos' % (nome.title(), idade))

# Exemplo de print 'moderno' 3.x
# print('{0} tem {1} anos' .format(nome.title(), idade))

# Exemplo de print 'mais atual' acima de 3.7
print(f'{nome} tem {idade} anos')

"""
# int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro.
"""
print(f'{nome} nasceu em {2022 - idade}')

# Transforma em uma lista de strings
print(f'{nome.split()}')







