"""
Módulo Collections - Counter
    Collections -> Hight-performance container datetypes (tipos de dados de container de alta performance)
Counter (contador) -> Recebe um interável como parâmetro e cria uma objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passado com o parâmetro e como valor
a quantidade de ocorrências desse elemento.


"""

# Realizando o import Counter

from collections import Counter

# Podemos utilizar qualquer interável, aqui usamos lista
lista = [1,1,2,3,4,4,5,1,2,3,5,5,6,6,6,6,6,6]

# Utilizando o Counter
res = Counter(lista)
print(type(res))
print(res)
#Counter({6: 6, 1: 3, 5: 3, 2: 2, 3: 2, 4: 2})
# para cada elemento da lista criou uma chave e colocou a quantiade de ocorrência
