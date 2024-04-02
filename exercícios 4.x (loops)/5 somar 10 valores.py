cont = 1
soma = 0
while cont < 11:
    valor = float(input(f'Qual o seu {cont}º valor: '))
    cont +=1
    soma += valor
print(f'A soma dos teus valores são {soma}')