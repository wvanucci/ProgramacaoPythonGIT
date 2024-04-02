qtd = int(input('Quantos números vc quer ver? \n'))
print('ORDEM CRESCENTE')
for i in range(0,qtd+1):
    print(i,end='; ')
print()
print('\nORDEM DECRESCENTE')
for i in range(qtd,-1,-1):
    print(i,end='; ')