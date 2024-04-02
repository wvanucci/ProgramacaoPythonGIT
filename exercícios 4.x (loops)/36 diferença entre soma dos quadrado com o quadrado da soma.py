cont=0
somaAoquadrado = 0
soma = 0
for i in range(1,101):
    soma += i
    a = pow(i,2)
    somaAoquadrado += a
result = somaAoquadrado - pow(soma,2)
print(f'{somaAoquadrado} - {pow(soma,2)} = {result}')