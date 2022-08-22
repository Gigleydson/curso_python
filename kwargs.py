"""
**Kwargs

Poderíamos chamar este parâmetro de **xix, mas por convenção chamamos de **Kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras
em uma tupla, o **Kwargs exige que utilizemos parâmetros nomeados, e transforma esses
parâmetros extras em um dicionário.

# Exemplo


def cores_favoritas(**kwargs):
    print(kwargs)


cores_favoritas(gigleydson='verde', izabela='rosa', joao='azul')


# Exemplo


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}!')


cores_favoritas(gigleydson='verde', izabela='rosa', joao='azul')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios.

cores_favoritas()

cores_favoritas(geek='preto')


# Exemplo mais complexo


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza de quem você é ...'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))


# Nas nossas funções, podemos ter (NESTA ORDEM):

- Parâmetros obrigatórios;
- *args;
- Parâmetro default (não orbigatórios);
- **kwargs


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Soleiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, 10, java=False, python=True)


# Desempacotar com **kwargs


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


# print(mostra_nomes(nome='Gigleydson', sobrenome='Dias'))

nomes = {'nome': 'Gigleydson', 'sobrenome': 'Dias'}
print(mostra_nomes(**nomes))

"""


def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = {'a': 1, 'b': 2, 'c': 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)
soma_multiplos_numeros(**dicionario)

# OBS: Os nomes da chave em um dicionário devem ser os mesmos dos parâmetros da função

# dicionario = {'d': 1, 'e': 2, 'f': 3}  # TypeError

