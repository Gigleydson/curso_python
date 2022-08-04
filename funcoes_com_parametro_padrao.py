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

"""
