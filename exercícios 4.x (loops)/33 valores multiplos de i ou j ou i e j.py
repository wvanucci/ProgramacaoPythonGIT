n = int(input('Qauntos nºnaturais: '))
i = int(input('Primeiro múltiplo: '))
j = int(input('Segundo múltiplo: '))
l = []

"""
COM WHILE E LISTA

cont =0

while len(l)<= n-1:  # temos fz mais um loop adicional colocanado n+1 termo entao temos q acrescentar o -1
    if cont % i == 0 and cont % j == 0:
        l.append(cont)
    elif cont % i == 0 and cont % j != 0:
        l.append(cont)
    elif cont % j == 0 and cont % i != 0:
        l.append(cont)
    cont += 1
print(l)
print(len(l))
"""
cont = 0
for g in range(0, n*2):
    if g%i==0 or g%j==0:
        cont=cont+1
        if cont<=n:
            print(g, end=' ')

