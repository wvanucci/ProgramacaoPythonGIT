# escrever na tela 1 até 100 de 1 em 1, 3x
print('Usando FOR')
for i in range(1,101):
    print(i,end=' ')
print('\nusando while')
num = 0
while num < 100:
    num += 1
    print(num)

print('\n Usando while break \n')

cont = 1
while cont > 0:
    print(cont)
    cont+=1
    if cont >100:
        break