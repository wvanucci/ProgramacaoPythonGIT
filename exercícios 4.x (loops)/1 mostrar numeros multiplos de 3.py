"""
determinar e mostrar os cinco primeiros múltiplos de 3 (só os maiores que zero)
"""

contador = 1
for i in range(1,100):
    if i%3 == 0:
        print(i)
        contador +=1
    elif contador > 5:
        break


