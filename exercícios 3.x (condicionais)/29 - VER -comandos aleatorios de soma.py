"""
from random import randint
print(randint(0,9))
Isto gera números inteiros entre 0 e 9.

É possível usar diversas outras funções disponíveis na documentação. Cada uma pode ser melhor para o que você deseja.

from random import randrange, uniform
print(randrange(0, 9)) #faixa de inteiro
print(uniform(0, 9)) #faixa de ponto flutuante
Você pode importar tudo e usar o que deseja:

from random import *
random.seed() #inicia a semente dos número pseudo randômicos
random.randrange(0, 9, 2) # pares entre 0 e 9
random.choice('abcdefghij') # seleciona um dos elementos aleatoriamente
items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items) # embaralha os itens aleatoriamente
"""

""" proa de somar inteiros menores que 100. Escolha nº aleatório entre 1-100 e pergunta a soma aleatoria
pedir 5 respostas mostrar quantas vezes acertou e errou"""

import random
contadorCerto = 0
contadorErrado = 0

for i in range(5):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    pergunta = int(input(f'Qual é a soma entre {a} e {b}? '))
    if pergunta == a +  b:
        print(f'Está certo. R: {a+b}')
        contadorCerto +=1
    else:
        print(f'Errado. R: {a+b}')
        contadorErrado += 1

print(f'Você acertou {contadorCerto} e errou {contadorErrado}')


