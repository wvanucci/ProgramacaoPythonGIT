n1= float(input('Digite um número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 < n2 < n3:
    print(f'{n1}, {n2}, {n3}')
elif n1 < n3 < n2:
    print(f'{n1}, {n3}, {n2}')
elif n2 < n3 < n1:
    print(f'{n2}, {n3}, {n1}')
elif n2 < n1 < n3:
    print(f'{n2}, {n1}, {n3}')
elif n3 < n1 < n2:
    print(f'{n3}, {n1}, {n2}')
elif n3 < n2 < n1:
    print(f'{n3}, {n1}, {n2}')

# outro modo
print()
lista = [n1,n2,n3]
lista.sort()
print(lista)
print(lista[0], lista[1], lista[2])