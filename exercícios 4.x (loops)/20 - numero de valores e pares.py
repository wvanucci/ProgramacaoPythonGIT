cont = 0
pares = 0

while cont>=0:
    valor = int(input('Digite um valor: '))
    cont += 1
    if valor%2 == 0:
        pares += 1
    if valor == 1000:    # não entendi pq elif nao roda o programa
        break

print(f'O número total lido é {cont} e o total de pares é {pares}')