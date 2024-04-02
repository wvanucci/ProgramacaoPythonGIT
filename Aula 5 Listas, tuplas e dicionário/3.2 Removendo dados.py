receita= {'jan':100,'fev':120,'mar':300}
receita.pop('fev')
# precisamos passar a chave no pop. Se não for encontrado vai dar erro

print(receita)
ret = receita.pop('mar')  #mais comum
print(ret)
print(receita)

#Ao removermos um objeto, o valor deste objeto sempre é retornado

#Forma 2
print('\n Forma dois para remover objeto de dict')

del receita['jan']
print(receita)
# OBS: Se a chave não existir será informado key error

