"""
Filter

filter() -> Serve para filtrar dados de uam determina coleção.

"""

# Por exemplo, filtar os valores acima do média

valores = 1, 2, 3, 4, 5, 6  # tupla

media = (sum(valores) / len(valores))

# print(media)

import statistics

# Biblioteca com dados estatísticos

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
# calcular média pela função mean()

media = statistics.mean(dados)
print(f'Média: {media:.4f}')
# OBS: Assim como a func map(), a filter recebe 2 parâmetros, sem uma função e um iterável.

res = filter(lambda x: x > media, dados) # funcao -> lambda x: x> media / iterável -> dados
# lambada recebe um parâmetro (x) de entrada (os elementos da lista dados) e será filtrado os dados acima da média
print(list(res))  # resultado
print(type(res)) # tipo filter
print(f'Novamente: {list(res)}') # assim como map, os dados são zerados, não fica na memória. Vantagem - memória vazia


