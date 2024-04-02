"""EP8 - python enhancement proposal
São propostas de melhorias para a linguagem python
the zen of python
import this


[ OBS: CTRL+K (ctrl+l) apaga o terminal no windows(linux). Ou o comando (no windowns)
>>> import os
>>> os.system('cls')    ]

A ideia da PEP8 é escrever códigos python de forma Pythonica.
Algumas importantes:


"""
""""[1] - Utilize Camel Case para nomes de classes:

    #certo:

class_Calculadora:  #começar com letra maiuscula
    pass
    #errado:
class_calculadora_cientifica:  #deve-se juntar nome composto diferenciando por letra maiuscula, por exemplo: calss_ClaculadoraCientfica
    pass"""

"""" [2] - Utilize nomes em minusculo separado por underline para funções ou variaveis

#certos

def soma():
    pass

def soma_dois():
    pass

numero_impar=4

#errado:

def Soma():
    pass

def somaDois():
    pass
"""
"""
[3] - utilize 4 espaços para identação! (PAR PYTHON)

#errado:
if 'a' in 'banana':
print('tem')

#certo
if 'a' in 'banana':
    print('tem')
    
    #no PYCHARM pode usar o tab(sempre verifique se tem quatro espaço):

if 'a' in 'banana':   #o dois ponto indica que vai começar outro blooo
    print('tem')
    
"""
"""
[4] - Linhas em branco
- separa funções e definições de classe com duas linhas em branco
-métodos dentro de uma classe devem ser separados com um única linha em branco
#certo


class Classe:
    pass
    
    
class Outra:
    pass
    
    """
"""[5]- imports
- imports dever ser sempre feitos em linha separadas

#errado

import sys,os

#certo:

import sys
import os 

    # não há problemas em utilizar: 
    
from type import StringType, ListaTypte

    # casso tenha muitos imports de um mesmo pacote, recomenda-se fazer:
    
from type imrpot(
    StringType,
    ListType,
    SetType,
    OutroType
)
    #Imports dever ser colocados no topo do arquivo, logo depois de quaisquer comentários ou
    docstrings e antes de constantes ou variáveis globais"""

"""[6] - Espaços em expressões e instruções

#não faça:

funcao( algo[ 1 ], { outro: 2 } )
algo (1)
dict ['chave'] = list [indice]
x       = 1
y    = 2

#faça:

funcao(algo[1], {outro: 2})
algo(1)
dict['chave'] = lsita[indice]
x = 1
y = 2"""

"""[7] - Termine sempre um instrução com uma nova linha
#fazer

print('Algo')

    #deixei uma linha em branco e finalizei"""
