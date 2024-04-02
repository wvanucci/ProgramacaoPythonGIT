print('\33[31mTransformando lista em tupla(vice-versa):\33[m')
lista = [1,2,3,4,5,6,7,0]
# transformando em tupla
tupla = tuple(lista)
print(tupla)
# transformando tupla em lista
lista2 = list(tupla)
print(lista2)

# desempacotamento de lista
print('\n\33[31mDesempacotamento de lista:\33[m')
lista3 = [1,2,3]
n1,n2,n3 = lista3
print(n1,n2,n3, end=' ')

# OBS: se tivermos mais elementos do que variavel para receber vai dar erro (vice-versa também vale)
