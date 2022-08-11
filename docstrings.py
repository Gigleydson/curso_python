"""
Documentando funções com Docstrings

OBS: Podemos ter acesso a documentação de uma função em Python
utilizando a propriedade especial __doc__

Podemos ainda fazer axesso a documentação com a função help()
"""

# Exemplos


def diz_oi():
    """Uma função simples que retorna a string Oi!"""
    return 'Oi!'


# print(diz_oi.__doc__)


def exponencial(numero, potencia):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' a 'potencia' infroamda.
    :param numero: Número que desejamos gerar o exponencial.
    :param potencia: Potência que queremeos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'.
    """
    return numero ** potencia


print(exponencial.__doc__)
print('')
help(exponencial)
