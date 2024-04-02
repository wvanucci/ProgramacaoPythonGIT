# se o nº for positivo -> raiz quadra se nao -> numero invalido
import math
n = float(input('Qual o seu número: '))
if n >= 0:
    rn = math.sqrt(n)
    print(f'A raiz de {n} é {rn:.4f}')
else:
    print('Número inválido')

