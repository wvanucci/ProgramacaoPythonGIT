""""
Listas
Listras em Python funcional como vetores/matries (arrays( em outras linguagens, com a diferença
se serem DINÂMICO e também de podermos colocar QUALQUER tipo de dado

Dinâmico:
    Linguagens C/Java: Arrays
        -POssuem tamanho e tipodedado fixo;
        Ou seja, nestaslinguagensse você criar um array do tipo int e com tamanho 5,
        este array será SEMPRE do tipo inteiro e poderá ter smepre no max 5 valores
    Já em Python:
      -Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente
      ir adicionando elemento

Qualquer tipo de dado: Não possuem tipo de dado fixo: ou seja, podemos qualquer tipo de dado

listas são representadas por colchetes (em python): []
"""

type([])
lista1 = [1,99,4,28,123,12,13123,55,464,1231]
lista2 = ['v','a','n','u','c','c','i']
lista3 = []
lista4 = list(range(11)) #list  transforma argumento em uma lista; rangecria elemento de 0 10
lista5 = list('Wilson Vanucci') #tem a msma funçao da lista 2 (mas nesse metodo ele adiciona o sstring ' ')

#Determinar se valor está contido na lista
print(lista1)
if 8 in lista4:
    print('Encontrei o número 8')
else:
    print('Não encontrei o número 8')

# podemos ordenar uma lista:
lista1.sort()
print('\033[31mordenando(sort)\33[m: ',lista1)
lista2.sort()  # ordem alfabetica
    # print(lista2)


# Contar o nº de ocorrencia de um valor:
    #print(lista1.count(1))
    #print(lista5.count('e'))

# Adicionar elemento em lista:
lista4.append(115)
 #print(lista4)
    # append só pode passar um argumento, porém:

lista1.append(['a','b','c']) # adicionando o elemnto ['a','b,'c'] em um elmento da lista1
print('\033[31mAdd em lista(append)\33[m: ', lista1)
    #já o extend adciona ITERAVEISS na lista:
lista1.extend([123,445,1233123123123123123123])
lista5.extend('Costa')
print('\033[31mAdd em lista(extend)\33[m: ',lista1)
print('\033[31mAdd em lista(extend)\33[m: ',lista5)

# podemos inserir um novo elemento na lista informando a posição
lista1.insert(2,'Novo Valor')
print('\033[31mAdd em lista(insert)\33[m: ',lista1)

#removendo termos
lista5.remove(' ')
print('\033[31mRemovendo variavel(remove)\33[m: ',lista5)

# podemos juntar duas lista
lista6 = lista1+lista5  #mesma coisa que o extend( lista1.extend(lista5))
print('\033[31moutro exempode soma\33[m:',lista6)

# Podemos facilmente inverter uma lista
lista1.reverse()
print('\033[31mRevertendo\33[m: ',lista1)  #print(lista1[::-1]) tbm reverte (esse método é usado para str)

