numero = str(input('digite um número entre 100 e 999: '))
numero2 = int(numero)  # convertendo string em inteiro
if numero2 < 100 or numero2 > 999:
    print('digite um número entre 100 e 999')
else:
    print(f'Número composto pelos algarismos: {numero[0], numero[1], numero[2]}')