"""refatorando funções"""


def diz_oi():
    return 'oi'


diz_oi()  # note, a função retorna "Oi" nao printou

print(diz_oi())

alguem = input("Qual seu nome: ")

print(f'{diz_oi()} {alguem}')

"""
Sobre a palavra reservada return

1 - Ela finaliza a função, sai da execucação da função
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos, uma uma função, retornar qualquer tipo de dados e até mesmo múltipls valores
"""

print("\nEXEMPLO 1 Ela finaliza a função, sai da execucação da função \n")


def diz_oi1():
    return 'oi'
    print('Estou sendo executado após retorno ...')


print(diz_oi1()) # depois do retorno nada é executado

print('\n Exemplo 2 Podemos ter, em uma função, diferentes returns;')

def nova_funcao():
    variavel = None  #posso botgar u minput para verificar mas é só mudar de True, False e None (diferentes returns) me condicional
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'
print(nova_funcao())

print('\n Exemplo 3 Podemos, uma uma função, retornar qualquer tipo de dados e até mesmo múltipls valores')

def outra_fun():
    return 2,3,4,5

print(outra_fun())  # lembrando que pega os dados e retorna em tupla
num1,num2,num3,num4 = outra_fun() #recebendo os dados e colocando nas variaveis
print(num1,num2,num3,num4)