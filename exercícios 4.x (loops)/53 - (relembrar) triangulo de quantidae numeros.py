n = int(input('Digite um número inteiro positivo: '))
soma = 0

for i in range(1, n + 1):
    soma += i
    for num in range(soma - i + 1, soma + 1):
        print(num, end=' ')
    print()

# ou

n = int(input(f'Digite o número de linhas: '))

valor = 1
for num in range(1, n + 1):
    print(f"N{str(num).zfill(2)} = | ", end='')  #.zfill(x) confere quantas str tem e completa x 0 na frente
    for i in range(1, num + 1):
        print(valor, end=' ')
        valor += 1
    print()