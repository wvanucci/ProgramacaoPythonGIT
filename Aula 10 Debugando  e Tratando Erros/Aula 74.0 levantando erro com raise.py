"""
Levantando os próprios erros com raise
raise - > Lança exceções

OBS: O raise não é uma função. É uma palavra reservada, assim como def ou qualquer outr a em Python.
Para simplificar, pense raise ocmo sendo útil para que possamos criar nossas próprias execeções e mensagens de erro

forma geral de utilização é

raise TipoDoErro('Mensagem')
OBS: O raise, finaliza o código/função, assim como o return
"""


# Exemplo - lançando quando ocorre erro especificando o erro

def colore(texto, cor):
    cores = ('verde','azul', 'vermelho', 'prata')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser um string')
    if type(cor) is not str:
        raise TypeError('core precisa ser uma string')
        print('Testando - Essa mensagem não será gerada pois existe um raise acima')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser um entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek','azul')

colore('Geek','Branco')
