# Função Quadrática com lambdada
def funquad(a, b, c):
    """retorna função quadrática"""
    return lambda x: a * x ** 2 + b * x + c


teste = funquad(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

#forma 2
print(funquad(2,3,-5)(1))  #função recebe os 3 parâmetros e se tem lambda tem que passar o último argumento para processar o lambda

print()