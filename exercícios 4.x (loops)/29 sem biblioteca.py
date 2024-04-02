# sum(n=0 to n ) n/((2n)!)
soma = 0
fat = 1
num = int(input('Informe o número desejado: '))
for i in range(1, num + 1):
    for j in range(1, 2 * i + 1):
        fat *= j
    soma += i / fat
    fat = 1
print(f'Soma final {soma}')