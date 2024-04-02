# verificar se o numero é primo ou nao


divisores = []

print('Você deve informar um número maior do que 1.')
num = int(input('Digite um número: '))
for i in range(1, num + 1):
    if num % i == 0:
        divisores.append(i)
if len(divisores) == 2 and divisores.__contains__(1) and divisores.__contains__(num):
    print(f'O número {num} é um número primo.')
else:
    print(f'O número {num} não é um número primo.')






