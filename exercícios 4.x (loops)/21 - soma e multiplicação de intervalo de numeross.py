"""
soma de numeros pares do intervalo digitado
multiplicação dos impares do intervalo digitado
"""

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
soma =0
mult = 1
for i in range(n1,n2+1):
    if i%2 == 0:
        soma += i
    elif i%2 != 0:
        mult *=i
print(f'A soma dos números pares do intervalo fechado de {n1} e {n2} é {soma}.\n'
      f'E a multiplicação dos números ímpares desse intervalo é {mult} ')