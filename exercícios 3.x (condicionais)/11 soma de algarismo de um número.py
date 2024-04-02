numero = input('Informe um valor: ')

soma = 0

for d in numero:
    soma = soma + int(d)
    print(d)
print(f'A soma de {numero} é {soma}')
