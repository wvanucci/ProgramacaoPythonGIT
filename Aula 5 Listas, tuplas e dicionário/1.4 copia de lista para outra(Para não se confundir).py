# copiando uma lsita para outra (Shallow copy e deep copyy)
print('\n\33[31mForma 1: Deep Copy\33[m')
lista = [1,2,3]
print(lista)

nova = lista.copy()

print(nova)
nova.append(4)

print(lista)
print(nova)

    # ao utiliza a lista.copy copiamos os dados para um nova lista, mas elas ficam independentes
    # ou seja, modificando uma lsita não afeta a outa. Isso se chama Deep Copy.

print('\n\33[31mForma 2: Shallow COpy\33[m')
lista1 = [1,2,3]
print(lista)

nova1 = lista1

print(nova1)
nova1.append(4)
print(lista1)
print(nova1)

    #A cópia via aatribuição (=) a modificação é realizada nas duas lista