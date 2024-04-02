r= int(input('Qual ang'))
rad = r * 3.141593 / 180
soma = 0
for i in range(6):
    prod = 1
    for p in range(1, (2 * i + 1)+1):
        prod *= p
    print(prod)
    x = ((-1) ** i / prod) * (rad ** (2 * i + 1))
    soma += x
    print(soma)
