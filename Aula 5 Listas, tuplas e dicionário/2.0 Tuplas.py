"""
Tuplas (tuple)
Parecidos com listas, mas... existe diferenças:

1- As tuplas são representadas por parênteses ()
    type(()) >>> tuple
2- As as tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda.
    Toda operação em uma tupla gera uma nova tupla.
    Exemplo de comparação com lista:
    #>>> lista = [2,1,3,4]
    #>>> lista.sort()
    #>>> lista
    [1,2,3,4}

    ou seja, estou mudando a lista com os métodos disponíveis, porém a tupla quando criada não é mutável (sort, append
    remove... não sao possiveis em tuplas)
________________________________________________________________________________________________________
# pode ser sem parenteses, porém deve ser um conjunto de valores separado por ,:
tupla1 = (1,2,3,4,5,6)
print(tupla1)
print(type(tupla1))

tupla2 = 1,2,3,4,5,6
print(tupla2)
print(type(tupla2))

#Cuidado 1: tupla com um elemento?
tupla3 = (3)  #não é uma tupla (não existe tupla de um número)
print(tupla3)
print(type(tupla3))  # vai retornar inteiro

# Cuidado 1.1: porém, se tiver só um elemento devemos inserir uma vírgula:
tupla4 = (4,)  #não é uma tupla (não existe tupla de um número)
print(tupla4)
print(type(tupla4))  # vai retornar inteiro

#CONCLUSÃO: TUPLA É DEFINIDA PELA VÍRGULA (,) ( A tupla2 podemos colocar só um elemento tupla2 = 1, -> é uma tupla)
    (4) -> não é tupla
    (4,) -> é tupla
    4, -> é tupla
"""
# gerar tupla com range:
tupla = tuple(range(2,15,2))
print(tupla)