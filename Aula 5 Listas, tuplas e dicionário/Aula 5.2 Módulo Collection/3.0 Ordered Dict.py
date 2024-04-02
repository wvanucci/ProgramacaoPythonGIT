"""
Ordered Dict - > É um dict que garante a ordem de inserção dos elementos

# em um dicionario, a ordem de inserção dos elementos não é garantida
dicionario = {'a':1,'b':2,'c':3,'d':4}
print(dicionario)
"""
from collections import OrderedDict

dicionario = OrderedDict({'a':1,'b':2,'c':3,'d':4})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

print('\n Fazendo diferença\n')
#Entendendoa diferença entre dict e OrderedDict
    #dicionarios comuns
dict1 = {'a':1,'b':2}
dict2 = {'b':2,'a':1}
print(dict1 == dict2) #retorna True já que a ordem dos elementos não importa para o dicionario

    #ordered dict
odict1 = OrderedDict({'a':1,'b':2})
odict2 = OrderedDict({'b':2,'a':1})
print(odict1==odict2) #False, já que a ordem importa para OrderedDict




