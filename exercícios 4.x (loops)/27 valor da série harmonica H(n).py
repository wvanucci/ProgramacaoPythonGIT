# série H(n) = 1 +1/2 ... 1/n
n=int(input('Digite um número: '))
h_n = 0
for i in range(1,n+1):
    h_n += 1/i

print(f'A série harmônica H(n) de 1 até {n} é {h_n:.5f}')