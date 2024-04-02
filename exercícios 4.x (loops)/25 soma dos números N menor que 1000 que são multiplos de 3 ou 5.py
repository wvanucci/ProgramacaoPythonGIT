# soma dos números N menor que 1000 que são multiplos de 3 ou 5
soma = 0
for i in range(0,1000):
    if i%3 == 0 or i%5 == 0:
        soma += i
print(f'A soma dos números N menor que 1000 que são multiplos de 3 ou 5 é {soma}')