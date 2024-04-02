receita = {'jan':10,'fev':200,'mar':400}
print(receita.values())

for valor in receita.values():
    print(valor)

#desempacotamento de dict
print('\nDesempacotamento de dict:')
print(receita.items())   #lista de tuplas contendo chave valor
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')