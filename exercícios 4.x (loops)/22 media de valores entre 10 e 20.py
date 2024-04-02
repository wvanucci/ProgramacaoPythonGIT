
cont, soma, media = 0, 0, 0

while cont >= 0:
    valor = float(input('Digite um valor: '))
    if 10 <= valor <= 20:
        soma+=valor
        cont+=1
        media = soma/cont
    elif valor > 20 or valor <10:
        print('O último valor digitado não está no intervalo aceitável')
        break
print(f'A média dos números aceitáveis é {media}')

