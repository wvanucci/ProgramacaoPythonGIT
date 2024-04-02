qt =int(input('Digite um valor: '))

print('ORDEM CRESCENTE')
for i in range(0,qt+1):
    if i%2 == 0:
        print(i,end='; ')
print()
print('\nORDEM DECRESCENTE')
for i in range(qt,-1,-1):
    if i%2 == 0:
        print(i,end='; ')