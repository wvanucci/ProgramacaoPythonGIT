# se o nº for positivo -> raiz quadra se nao -> numero ao quadrado
n = float(input('Digite um número: '))
raiz_n = n**(1/2)
aoQuadradoDen = n**2

if n >= 0:
    print(f'A raiz de {n} é {raiz_n:.3f}')
else:
    print(f'O quadrado de {n} é {aoQuadradoDen}')

