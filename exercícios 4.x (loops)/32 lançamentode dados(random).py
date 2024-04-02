"""
simula lançamento de dois dados d1 e d2,n vezes, e tem como saída número de cada dado
e a realação entre eles (>,<,=) de cada lançamento
"""
import random
vezes = int(input('Quantas vezes você quer realizar a operação: '))
cont = 1
while cont <= vezes:
    a = random.randint(1,10)
    b = random.randint(1,10)
    if a < b:
        print(f'{a} < {b}')
    elif a > b:
        print(f'{a} > {b}')
    elif a == b:
        print(f'{a} = {b}')
    cont+=1
