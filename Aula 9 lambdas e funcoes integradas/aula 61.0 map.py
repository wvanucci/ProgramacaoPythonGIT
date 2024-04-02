"""
Map

-IPC para datasciece; Trabalhando com coleçoes de dados em datascience
Com map, fazemos mapeamento de valores da função
"""

import math

def area(r):
    """Calculo de área de um círculo"""
    return math.pi*(r**2)

print(area(2))
print(f'{area(5.3):.4f}')

raios = [2, 5, 7.1, 0.3, 10, 44]

#forma commum
areas=[]
for r in raios:
    areas.append((area(r)))

print(areas)

#Forma 2 - map
print()
#map é uma função que rebe dois parâmetros: O primeiro a função, o segundo um iterável

areas = map(area, raios)
print(areas)  #map é um outro objeto (não é uma lista uma tupla ou dict) = Map Obejct
print(type(areas)) #conferindo o tipo
print(list(areas)) #transformando map para lista
print(tuple(areas)) #transformando map para tupla

#Forma 3 - map com lambada
print()
print(list(map(lambda r: math.pi*r**2, raios)))
# explicando: cada item da lista raios é o argumento para o parâmetro r da funcao anonima lambda

#OBS: Após utilizar a função map(), depois da primeira utilização do resultado, ele zera
#é interessante pois limpa a memória