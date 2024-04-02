"""Range é método auxiliar
 - precisando conhecer loop for para usar o range
 - precisamos conhecer range para trabalhar melhor com loop for.

 Ranges são utilizados para gerar sequencias numéricas, não de forma aleat´ória mas
 mas sim de maneira especifícada

Formas gerais

    #forma 1
range(valor de parada)
OBS: valor de para não inluida (começa do 0 com passo de 1 em 1)
exemplo:

for n in range(11):
    print(num)

    #forma 2
range(valor de inicio, valor de parada)
OBS: valor de parada nao incluido (começa do inicio com passo 1 em 1)
Exemplo:

for n in range(1,10):
    print(n)

    #forma 3
range(valor de inicio, valor parada, passo)
OBS: valor de parada não incluido( começa vinicio ccom passo definido)
exemplo:

    for n in range(2,10,2):
        print(n,end=' ')  # o end = ' ' só para fazer na msm linha separando com  ' 'cada valor

    # forma 3.1 inverso (contagem regressiva)
range(valor inicio, valor de parada, -passo)
valor de parada não incluido
exemplo:

    for n in range(10, 0, -1):
        print(n, end= ' ')
"""
for n in range(2,10,2):
    print(n,end=' ')

print()

for n in range(10, 0, -1):
    print(n, end=' ')

#posso acrescentar range em uma lista
print()
lista = list(range(19,-1,-2))
print(lista)

