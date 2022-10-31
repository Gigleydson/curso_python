"""
Levantando os próprios erros com raise

raise -> Lança exceções

OBS: O raise não é uma funçãpo. É uma palavra reservada, assim como o def ou qualquer outra em Python.

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens de erro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de erro')

# Exemplo real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    elif type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('XBOX', 'verde')


Exemplo refaturado

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'branco', 'azul')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    elif type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    elif cor not in cores:
        raise ValueError(f'cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('XBOX', 'preto')

OBS: O raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado.
"""

# Exemplo real


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'branco', 'azul')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    elif type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    elif cor not in cores:
        raise ValueError(f'cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('XBOX', 'preto')
