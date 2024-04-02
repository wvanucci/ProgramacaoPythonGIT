""" se digitar um numero negativo o program para
"""

cont = 0
verificar = 0
n = int(input('Digite um número: '))
maior = n
menor = n
while cont >= 0:
    n = int(input('Digite um número: '))
    if n < 0:  # o parar tem q vim antes de atribuir as variaveis maior e menor
        break
    if n > verificar:
        maior = n
    if n < verificar:
        menor = n
    verificar = n


print(f'O maior núemro digitado: {maior}. Menor número digitado: {menor}')

