cont = 1
n = int(input('Digite um número: '))
h_n = 0
while True:
    if cont <= n:
        h_n += 1/cont
        cont += 1
    else:
        break
print(f'A série harmônica H(n) de 1 até {n} é {h_n:.5f}')