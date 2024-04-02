valores = ['oi', 2, 3, 4]
# acessar termo da lista
print('\33[31mAcessando termo com [posição]e [-posição]:\33[m')

print(valores[0])
print(valores[2])
print(valores[-1])
print(valores[-2])
print(valores[-4])
# gerar índice em um for:
print('\n\33[31mGerar indices de lista:\33[m')
for indice,valor in enumerate(valores):   # enumerate gera tuplas com chave e valor
    print(indice, valor)

print('Mostrando o enumerante:',list(enumerate(valores)))

# mostrar o indice que corresponde o elemento:
print('\n\33[31mMostrar o índice que corresponde o elemento:\33[m')
print('  \33[31m   Exemplo 1:\33[m')
print(valores)
print(valores.index('oi'))
# OBS: se o elemento não estiver na lista vai dar erro
print('  \33[31m   Exemplo 2:\33[m')
numeros =[3,1,4,1,1,5]
print(numeros)
print(numeros.index(1)) # retorna o indice do primeiro valor encontrado
print('  \33[31m   Exemplo 3:\33[m')
print(numeros)
print(numeros.index(1,2)) # qual o indice de 1 a partir do indice 2
print('  \33[31m   Exemplo 4:\33[m')
print(numeros)
print(numeros.index(1,4,5)) # mostrar indice de 1 entre os indices 4 até 5

#revisa slicing para lista-> (inici0, fim, passo) (semelhante a range e str (interavel)):
print('\n\33[31mUsando método slice:\33[m')
lista1 = [1,2,3,4]

print('  \33[31m   Mostar a partir de um índice. Exemplo 1:\33[m')
print(lista1)
print(lista1[1:]) # msotrar todos os elementos iniciando do indice 1

print('  \33[31m   Mostrar até um (índice-1). Exemplo 2:\33[m')
print(lista1)
print(lista1[:2]) # msotrar todos os elementos até o indicie 2-1

print('  \33[31m   Mostrar com inicio, final e passo. Exemplo 3:\33[m')
print(lista1)
print(lista1[0:len(lista1)+1:2]) # msotrar os elementos de 0 até último termo e passo 2
                                # (podemos colocar [::2} para colocar só o passo de toda lista)

print('  \33[31m   Invertendo a lista. Exemplo 4:\33[m')
print(lista1[::-1])
print('Mostrando invertido e com passo: ',lista1[1::-1])