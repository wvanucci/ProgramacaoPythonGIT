start = 0
fim = 50
resto = start % 2
soma = 0

while resto != 0 or start <= fim:
    resto = start % 2
    if resto == 0:
        print(start)
        soma = soma + start
        start = start + 1
    else:
        start = start + 1

print(f'A soma de tudo é {soma}.')