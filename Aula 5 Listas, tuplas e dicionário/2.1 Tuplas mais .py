# desempacotamento de tupla
    # atribuir variáveis para cada elemento da tupla
tupla = ('oi','tchau')
bemvindo, flws = tupla
print(bemvindo)
    #OBS: Gera erro se colocarmos um valor diferente do elementos para desempacotar

# Métodos para remoção e adição nas tuplas não existem (tuplas são imutavéis)

# métodos para obter informações da tupla é possível (min, max, sum, len)
    #* lembrando que min, max e sum só funcionam se os elmentos forem int ou float

# concatenação de tuplas (juntar tuplas) é possível (mas as originais não se alterma pois são imutveis)
print('\n\33[31mConcatenação:\33[m')
tupla2 = 4,5,6
print(tupla2)

print(tupla2+tupla)

print(tupla)
print(tupla2)

# mas é possivel alterar a tupla sobrescrever:
print(tupla)
tupla=tupla+tupla2
print(tupla)

# interando em tupla:
print('\n\33[31mInterando:\33[m')

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice,valor)

#contando elemento um tupla:
print('\n\33[31mContando elemento em tupla:\33[m')

tupla3 = ('a','b','c','a')
print(tupla3.count('a'))

# convertendo str em tupla
print('\n\33[31mConvertendo str em tupla:\33[m')
escola = 'jose pedro e taus'
tuplaescola = tuple(escola)
print(tuplaescola)