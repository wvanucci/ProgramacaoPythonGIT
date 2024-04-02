# soma de ivisores de um número exceto ele próprio
numer = int(input('Digite um número: '))
soma = 0
for i in range(1,numer):
    if numer%i == 0:
        soma += i
        print(f'{numer} é divisível por {i}')
print(f'A soma desses números é {soma}')
