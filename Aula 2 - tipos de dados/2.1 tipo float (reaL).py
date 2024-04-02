""""
Tipo float (real, com casas decimais)

OBS: O separador de casas decimaisna programação é o ponto (.) e nãoa vírgula (,)
        certo:
        valor = 1.4
        errado:
        valor = 1,4  (em python valo é uma tupla -> (1,4))
"""

# é possivel fazer dupla atribuição:

r = valor1, valor2 = 2.3, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

    # note que se atribuir r ccomo uma variavel da dupla atribuição:

print(r)
print(type(r))

    # podemos pegar o inteirodo float:
k = int(valor1)
print(k)
print()   # é somente para pular linha

""" para criar uma variável complexa é atribuida um 'j'(=RAIZ(-1)=i) veja exemplos:"""
print('Nº C O M P L E X O ')
print()

complexo = 5j
print(complexo)
print(type(complexo))
print(complexo**2)

