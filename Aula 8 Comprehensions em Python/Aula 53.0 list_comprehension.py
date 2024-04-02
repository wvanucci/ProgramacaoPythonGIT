"""
List Comprehension
    - Utilizando nós podemos gerar novas listas com dados processados a partir com outro interável.
#Sintaxe
    [dado for dado in iterável]
"""
import math

num = [1,2,3,4,5]

res = [n*10 for n in num] #cada elemento n da lista num será multiplicado por 10 e vai me retornar uma lista atribuida em res

print(res)

"""
Para entender melhor o que está acontecendo:
-primeira parte: for n in num
-segunda parte: n*10
"""

res = [math.floor((n/3)*1000)/1000 for n in num]  #math.floor e *1000 /1000 para truncar em 3 deciamis
print(res)