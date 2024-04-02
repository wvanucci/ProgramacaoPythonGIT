numero = int(input('Digite um numero entre 100 e 999: \n'))
contador = 1
for i in str(numero):     #variaveis int e float não sao interaveis portanto transformei em str
    if 100 <= numero <= 999:
        print(f'Seu {contador}º algarismo é {i}')
        contador += 1
    else:
        print('Seu número não está entre 100 e 999')