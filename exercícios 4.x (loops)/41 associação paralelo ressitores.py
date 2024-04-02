
while True:
    r1 = int(input('Digite resitência R1: '))
    r2 = int(input('Digite resitência R2: '))
    if r1 <= 0 or r2 <= 0:
        break
    else:
        rEqui_div_por_1 = 1/r1 +1/r2
        Requi = 1/rEqui_div_por_1
        print(f'Resistência equivalente em paralelo é: {Requi}')

# uma forma geral
resistenciaPorUm = 0
qtd = int(input('Quantos resistores têm nessa associação em paralelo? '))
for i in range(1,qtd+1):
    resistencia = int(input(f'Resistência do resistor {i}: '))
    resistenciaPorUm += 1/resistencia

print(f'Resistência equivalente em paralelo é: {1/resistenciaPorUm}')
