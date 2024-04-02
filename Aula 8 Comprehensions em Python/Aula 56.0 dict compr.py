"""
Dictionary Comprehension

Pense no seguinte:
    Se quisermos criar uma lista fazemos:
    lista=[1,2,3,4]

    Se quisermos criar uma tupla:
    tupla = (1,2,3,4) #1,2,3,4

    se quisermos criar um set (conjunto)

    conjuunto = {1,2,3,4}
    Se  quisermos criar um dict

    dicionário = {'a':1,'ba':2,}

#sintaxe

{chave:valor for valor in interavel} dict comprehe
[valor for valor in interável] list compre
"""

num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# print(num.items())
quadrado = {chave: valor ** 2 for chave, valor in num.items()}  # num.items() devolve lista de  tupla
print(quadrado)

print()

l = [1,2,3,4]

quad = {valor: valor**2 for valor in l}  # colocar os itens de uma lista em dict. valor original = key e valor**2 = valoues
print(quad)

# para tupla e set é a mesma coisa
#lembrando que não existe repeticao de chaves no dict, então se alguma valor se repetir na lista/tupla/set só vai contar
#uma vez

#exemplo
print()
l = (1,2,3,4,2,4,4)

quad = {valor: valor**2 for valor in l}  # colocar os itens de uma lista em dict. valor original = key e valor**2 = valoues
print(quad)

print()
print('exemplo2 \n')
#exemplo2
chave = 'abcde'
valores=[1,2,3,4,5]

mistura={chave[i]: valores[i] for i in range(0, len(chave))}
print(mistura)
