# se o nº for positivo -> raiz quadra e ao quadrado
n = float(input('Digite um número: '))


if n >= 0:
    raiz_n = n ** (1 / 2)
    aoQuadradoDen = n ** 2
    print(f'O quadrado de {n} é {aoQuadradoDen} e sua raiz quadrada é {raiz_n:.5f}')
else:
    print('Esse número é negativo')

