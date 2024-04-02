"""
Sorted
Obs: Não confunda, apesar do nome, com a função sort() que já estudamos em Listas. O sort() só funciona em listas

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar

sort() só funciona para lista
sorted() para qualquer iterável
"""

# Exemplo
numeros = {6, 1, 8 , 2}
print(sorted(numeros)) # ordenar do menor para maior
print(numeros)
# sorted não modifica o objeto, no caso do sort ( aplicado na lista) modifica a lista
print()

num = (1,3,2,12,22,11)
print(sorted(num)) # retorna uma lista ordenada
print(num)

print('\nExemplo de sorted()\n')
# adicionar parâmetros ao sorted()

print(sorted(numeros, reverse = True )) # Ordena do maior para o menor
#podemos converter sorted
print(tuple(sorted(numeros, reverse = True )))