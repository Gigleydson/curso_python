"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

Toda entrada do usuário deve ser tratada!

OBS: A função do usuário é destruir o seu sistema.

# Else -> É executado somente se não ocorrer o erro.

# Exemplo

try:
    num = int(input('Digite um número: '))
except ValueError:
    print("Valor inválido!")
else:
    print(f'O número digitado foi {num}')


# Finally

# Exemplo

try:
    num = int(input('Digite um número: '))
except ValueError:
    print("Valor inválido!")
else:
    print(f'O número digitado foi {num}')
finally:
    print('Executando o finally')

# OBS: O bloco finally é SEMPRE executado. Independente se houver execução ou não.

# O finally, geralmente é utilizado para fechar ou desalocar recursos.


# Exemplo mais complexo - Errado


def dividir(a, b):
    return a / b


try:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
except ValueError:
    print('Digite valores numéricos!')
else:
    print(f'O resultado é', dividir(num1, num2))


# Exemplo mais complexo - Correto
# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto!'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero.'


num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')
print(dividir(num1, num2))


# Exemplo mais complexo - Genérico
# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!


def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema!'


num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')
print(dividir(num1, num2))
"""

# Exemplo mais complexo - Semi-Genérico
# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')
print(dividir(num1, num2))
