"""
Faça um programa que some os números impares contidos em um intervalo definido pelo usuário.
O usuário define o valor inicial do intervalo e o valor final deste intervalo e
o programa deve somar todos os números ímpares contidos neste intervalo.
Caso o usuário digite um intervalo inválido (começando por um valor maior que o valor final)
deve ser escrito uma mensagem de erro na tela, “Intervalo de valores inválido” e o programa termina.
Exemplo de tela de saída: Digite o valor inicial e valor final: 5 10 Soma dos ímpares neste intervalo: 21
"""

n1 = int(input('Digite o valor inicial: '))
n2 = int(input('Digite o valor final: '))
soma =0
for i in range(n1,n2+1):
    if i%2 !=0:
        soma+=i
print(f'Soma dos ímpares neste intervalo: {soma}')