soma1 = 0
soma2 = 0
soma3 = 0
lista = []
hab = int(input('Digite o número de habitantes: '))
for c in range(1, hab + 1):
    print('\nOPÇÕES''\n[1] Residencial''\n[2] Comercial''\n[3] industrial')
    tip_cons = int(input(f'Para o habitante número {c}, qual o tipo de consumidor ele é?: '))
    if tip_cons == 1:
        kwh1 = float(input('Qual o consumo deste habitante: '))
        soma1 = soma1 + kwh1
        lista.append(kwh1)
    if tip_cons == 2:
        kwh2 = float(input('Qual o consumo deste habitante: '))
        soma2 = soma2 + kwh2
        lista.append(kwh2)
    if tip_cons == 3:
        kwh3 = float(input('Qual o consumo deste habitante: '))
        soma3 = soma3 + kwh3
        lista.append(kwh3)
print(f'O menor consumo entre todos os habitante: {min(lista):.2f}')
print(f'O maior consumo entre todos os habitantes: {max(lista):.2f}')
print(f'A média do consumo de todos os habitantes: {(soma1 + soma2 + soma3) / 3:.2f}')
print(f'A soma do consumo das Residências: {soma1:.2f}')
print(f'A soma do consumo dos Comércios: {soma2:.2f}')
print(f'A soma do consumo das industrias: {soma3:.2f}')