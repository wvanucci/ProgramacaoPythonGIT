numero = int(input('Informe um número: '))

numero += 1
while True:
    if not numero % 11:
        print(f'O número {numero} é múltiplo de 11.')
        break
    if not numero % 13:
        print(f'O número {numero} é múltiplo de 13.')
        break
    if not numero % 17:
        print(f'O número {numero} é múltiplo de 17.')
        break
    numero += 1