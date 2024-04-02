"""
OBS: Diferende de reverse() - é aplciada só em lista

reversed() funcina com qualquer iterável (mesma lógica de sorted) ela inverte iterável

retorna um objeto do tipo list_reverseiterator

Sua função é inverter o iterável.
"""
# Exemplos
lista = [1,2,3,4,5,6]
res = reversed(lista)

print(res)
print(type(res))

#convertendo o objeto
#print(set(res))
#print(tuple(res)) # mesmo esquema de sorted / genberator. Não guarda na memória

#mas...
print(tuple(reversed(lista)))
print(list(reversed(lista)))
print(set(reversed(lista))) # set é imutáveçl


