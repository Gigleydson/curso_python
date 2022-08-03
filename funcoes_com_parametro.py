"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas não possuem saída;
- Possuem entrada e saída;


# Exemplo 1 - Função que recebe parâmetro

def quadrado(numero):
    # return numero * numero
    return numero ** 2  # elevando o número ao quadrado.
    # return numero ** 3  # elevando o número ao cubo.


print(quadrado(7))
print(quadrado(5))
print(quadrado(10))

ret = quadrado(9)
print(ret)

print(quadrado())  # TypeError


# Refatorando a função catar_parabens()

def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nessa data querida')
    print('Muitas felicidaes')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}!')


cantar_parabens('Gigleydson')


# Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada
# em uma função quantos parâmetros forem necessáros. Eles são separados por vírgula.

# Exemplos

def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num3, b, msg):
    return (num3 + b) * msg


print(soma(2, 3))
print(multiplica(2, 5))
print(outra(4, 6, 'Resultado '))


# OBS: Se a gente informar um número errado de parâmetro ou argumentos, teremos TypeError

# print(soma(2, 3, 4))  # TypeErros - Passando argumentos a mais
# print(soma(2))  # TypeErros - Passando argumentos a menos


# Nomeando parâmetros

def nome_completo(nome, sobrenome):
    return f'O seu nome completo é {nome} {sobrenome}'


print(nome_completo('Gigleydson', 'Dias'))


# A diferença entre Parâmetros e Argumentos

# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;
# A ordem dos parâmetros importa!

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los,
# podemos utilizar qualquer ordem.

# Exemplo
print(nome_completo(sobrenome='Álvaro', nome='João'))
"""


# Erro comum na utilização do return

"""
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
        return total  # retorna apenas o primeiro número ímpar
"""


# Maneira correta

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total  # retorna a soma de todos os números ímpares passados no parâmetro.


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(soma_impares(lista))
