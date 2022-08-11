"""
Funções com Parâmetro Padrão (Default Paramters)

- Funções onde a passagem de parâmetro seja opcional;

# Exempro de função onde a passagem de parâmetro seja opcional
print('Geek Universety')
print()


# Exemplo de função onde a passagem de parâmetro seja obrigatório
def quadrado(numero):
    return numero ** 2


print(quadrado(5))
print(quadrado())  # TypeError


def exponencial(numero, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))  # 2 * 2 * 2 = 8
print(exponencial(3, 2))  # 3 * 3 = 9
print(exponencial(5))  # Por padrão eleve ao quadrado
print(exponencial(3, 3))  # Eleve a potência informada pelo usuário

# OBS:
# Se o usuário passar somente 1 parâmetro, este será atribuído número e será calculado o quadrado deste número
# Se o usuário passar 2 argumentos, o primeiro será atribuído ao parâmetro número e o segundo ao parâmetro potencia
# Então será calculada esta potência


# OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração

# ERROR!
def teste(num=2, potencia):
    return num ** potencia


# Correto
def teste2(potencia, num=2):
    return num ** potencia


print(teste2(2))


# Exemplo mais complexo

def mostra_informacoes(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você fosse o instrutor'
    return f'Olá {nome}'


print(mostra_informacoes())
print(mostra_informacoes(instrutor=True))
print(mostra_informacoes(True))
print(mostra_informacoes('Gigleydson'))

# Por quê utilizar parâmetros com valor default?

- Nos permite ser mais flexíveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código

# Quais tipos de dados podemos utilizar como valores default para parâmetros?

- Qualquer tipode dado:
    -   Números, string, floats, booleanos, listas, tuplas, dicinários, funções e etc;

# Exemplos

def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


print(soma(6, 4))
print(mat(6, 4, subtracao))


# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek'  # Variável global


def diz_oi():
    # instrutor = 'Python'  # Variável local
    return f'Oi {instrutor}'


print(diz_oi())

# OBS: Se tivermos uma variável localo com o mesmo nome de uma variável global, a local terá preferência.


def diz_oi():
    prof = 'Geek'  # Variável local
    return f'Oi {prof}'


print(diz_oi())

print(prof)  # Variável só existe detro da função, por isso da o erro 'NameError'


# ATENÇÃO com variáveis globais (Se puder evitar, evite!)

total = 0


def incrementa():
    total = total + 1  # UnboundLocalError - Variável local sendo utilizada para processamento sem ter sido inicializada
    return total


print(incrementa())


def incrementa():
    global total  # Avisando que queremos utilizar a variável global
    total = total + 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())
"""

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escolpo de variável


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador += 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())

print(dentro())  # NameError
