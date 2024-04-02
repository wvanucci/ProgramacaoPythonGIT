primo = []
lista = []
cont = 1

while cont < 20000:
    for i in range(1, cont + 1):
        if cont % i == 0:
            lista.append(i)

    if len(lista) == 2:
        primo.append(cont)
        lista.clear()
    else:
        lista.clear()
    cont += 1
print(primo)
print(sum(primo))