"""
Zip

zip() -> Cria um iterável (zip object) que agrega elemento de  cada um dos iteráveis passados com entrada em pares.
 - junta cada elemento da cada iterável
 - devolve pares de tupla
 - em dict  devolve chave: valor
 -quantidade de combinações é definida pelo iterável de menor elemento
    não existe combinação vazio; somente se existir vazio da forma ''
    - podemos utilizar diferentes iteráveis com zip

"""

l1 = [1,2,3,4,5]
l2 = [5,6,7,8, 2]

zip1 = zip(l1,l2, 'abcdfasdasd')
print(zip1)
print(type(zip1))

# sempre podemos gerar uma coleçao do zip object

print(list(zip1))
print(tuple(zip1)) # assim que é convertido para lista some da memória
print(set(zip1))