# podemos utilizar qualquer tipo de dado(int, float, str, bool), inclusive lista, tupla dic, como chaves
# de dicionários

localidades = {
    (31.534,39.323):'Escritório em Tókio',
    (40.123, 78.123): 'Escritório em NY',
    (12.1231,15.1231): 'Escritório Buenos'
}

print(localidades)
print(localidades.get((31.534,39.323)))

#Forma 1
print('\n Adicionando dado, forma 1:')
receita= {'jan':100,'fev':120,'mar':300}
print(receita)
receita['abr']=350
print(receita)
# forma 2. Add dados:
print('\n Adicionando dado, forma 2:')
novo_dado = {'mai':500}

receita.update(novo_dado)
print(receita)

#CONCLUSÃO 1:A forma de adiconar novos elementos ou atualizar dados em um dict é a mesma
#OBS;Em um dict não podemos ter uma mesma chave


