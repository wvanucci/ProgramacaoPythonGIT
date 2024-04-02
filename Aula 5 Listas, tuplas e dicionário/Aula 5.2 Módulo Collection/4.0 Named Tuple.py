"""
Named Tuple -> São tuplas, diferenciadas, onde, especificamos um nome para a mesma e também parâmetros
"""

from collections import namedtuple

#precisamos definir o nome e parâmetros:

    #forma 1 - Declaração Named Tuple
cachorro = namedtuple('cachorro','idade raça nome')
    #forma 2 - Declaração Named Tuple
cachorro = namedtuple('cachorro','idade, raça, nome')
    #forma 3 - Declaração Name TUple (mais bonita)
cachorro = namedtuple('cachorro',['idade','raça','nome'])

#Usando
ray = cachorro(idade=2, raça='vira-lata', nome='ray')
print(ray)#CRIANDO  um dado próprio

#acessando dados forma 1

print(ray[0])
print(ray[2])

    #forma 2
print()
print(ray.idade)
print(ray.raça)
print(ray.nome)

print()
print(ray.index(2))
print(ray.count('vira-lata'))