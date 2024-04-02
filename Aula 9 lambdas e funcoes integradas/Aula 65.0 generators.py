"""
Generators

Em aulas anteriores nós estudamos:
-List comprehension
- Dictionary comprehension
- Set comprehension

Não vimos:
- Tuple comprehension... porque elas se chamam generators


"""
nomes = ['Carlos', 'Catarina', 'Cassiano']
print((nome[0] == 'C' for nome in nomes)) # salva como objeto nao reorna nada,
res=(nome[0] == 'C' for nome in nomes)

from sys import getsizeof
# Utilidade de getsizeof() retorna a quantidade de bytes em memória do elemento

print(getsizeof(222))
print(getsizeof(True))

print(getsizeof(1))
print(getsizeof(1231233131))