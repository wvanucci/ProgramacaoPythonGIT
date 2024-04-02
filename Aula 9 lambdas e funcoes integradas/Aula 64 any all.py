"""
funções integradas: Any e All

all() -> retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.
"""

# Exemplo all()

print(all([0,1,2,3,4,5])) # Todos os números são verdadeiros (0 é false) -> retorna False
print(all([]))
print(all((1,3,4,)))
print(all({}))

# Exemplo viável
print()
nomes = ['Carlos', 'Catarina', 'Cassiano']
print(all([nome[0] == 'C' for nome in nomes]))

"""
any() - > retorna True se qualquer elemento do iterável for vcerdadeiro. Se o iterável estivar vazio, retorna False
"""
print('\nExemplo 2 \n')

print(any([0,1,2,3,4,5])) # True
print(any([0, False, {},  (), []])) # False tem TODOS os iteráveis vazios


