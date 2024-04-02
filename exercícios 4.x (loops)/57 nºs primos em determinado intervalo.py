primo = []
lista = []
cont = 1
a=int(input('Start: '))
b=int(input('FInal: '))
while cont <= b:
    for i in range(a, b + 1):
        if cont % i == 0:
            lista.append(i)

    if len(lista) == 2:
        primo.append(cont)
        lista.clear()
    else:
        lista.clear()
    cont += 1
print(primo)
print(f'Existem {len(primo)} números primo entre {a} e {b}')
print(f'A soma dos primos entre {a} e {b} é {sum(primo)}')