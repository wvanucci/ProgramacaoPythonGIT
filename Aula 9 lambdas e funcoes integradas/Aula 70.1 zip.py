# podemos utilizar diferentes iteráveis com zip

lista =[1,2,3,4,5]
tupla = 6,7,8,94,2
dic = {'a':123,'s':3123,'h':12,'2':124}

zt = zip(lista, tupla, dic.values())
print(list(zt))

dados=[(0,1),(1,2),(2,3)]
print([*dados])
print(list(zip(*dados))) # * descompacta
