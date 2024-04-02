""" Dados Faltantes
"""

paises = ['', 'Argentina', '', 'Brasil', 'Chile', ' ', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)
#FORMA 1
res = filter(None, paises) #filtar na lista paises os dados None (vazio)

print(list(res))

#FORMA 2 LAMBADA
print()
res1 = filter(lambda x: len(x) > 0, paises) # pegar só as string com tamanho maior que zero. Note que ' ' é uma str
                                            #com espaço e não vazio
print(list(res1))

#uma solução
print()
res1 = filter(lambda x: x != '' and x != ' ', paises)
print(list(res1))