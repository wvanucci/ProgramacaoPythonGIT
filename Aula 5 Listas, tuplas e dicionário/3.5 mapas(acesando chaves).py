"""
Mapas-> conhecidos em Python como dicionários

Dicionários em Pyton são representados pro chaves {}
"""

receita = {'jan':10,'fev':200,'mar':400}

print(receita)

#interar sobre o dic
for chave in receita:
    print(chave)  #imprimi a chave
    print(receita[chave])  #imprimi o valor
    print(f'Em {chave} recebi R${receita[chave]}\n')

#mas para conhecer todas as chave

print('Dict de chave (acesando chaves):')
print(receita.keys())  #dict keys lista de chaves


#modo pythonico para interar dict
print('\nModo Pythonico')
for chave in receita.keys(): #acesso cada termo da dict keys (lista de chaves da receita)
    print(receita[chave])

