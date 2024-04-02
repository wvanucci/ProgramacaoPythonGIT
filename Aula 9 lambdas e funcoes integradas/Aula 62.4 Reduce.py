"""
Reduce
OBS: A partir do Python 3+ a função reduce() nao é mais uma função integrada (built-in). Agora temos que importar e utilizar
esta função a partir do módulo 'functools'

Guido van ROssum: Utiliza a função reduce() se você realmente precisa dela. Em todo caso,
99% das vezes um loop for é maislegível.

Para entender reduce()
# Imagine um coleção de dados:
dados = [a1,a2,...an]

# E você tem uma função qeu recebe dois parâmetros:

def funcao(x,y):
    return x*y

Assim como map() e filter(), a função reduce() recebe dois parâmetros: a função e o iterável
a função reduce (), funciona da seguinte forma:
    Passo 1: res1 = f(a1,a2) # Aplica a função nos dois primeiro elementos da coleção e guarda o resultado
    Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo1 mais o terceiro elemento

    Isso é repetido até o final.
    Passo 3: res3 = f(res2, a4)
    .
    .
    .
    passo n; resn = f(resm, an)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterio. No final,
reduce() irá retornar o resultado final.

Alternativamente, poderíamos ver a função reduce() como:

funcao(funcao(funcao(a1, a2),a3 ),a4),..),.. an)
"""

#Exemplo - utilizar reduce() para multiplicar os números de uma lista

from functools import reduce
dados = [1,2,3,4,5,123,21,12,4,5,6]

# Para utilizar o reduce() nós precisamos de uma função que receba dois parâmetros
multi = lambda x, y: x*y
res = reduce(multi, dados)
#1*2*3*4...
print(res)

#exemplo com o for
j=1
for i in dados:
    j=i*j

print(j)