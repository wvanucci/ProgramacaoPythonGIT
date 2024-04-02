#logaritimo de um nº positivo
import math
n = float(input('Digite um número: '))
if n > 0:
    print(f'O logaritimo de {n} na base 10  é {math.log(n,10)}')
else:
    print('O numero é negativo')
