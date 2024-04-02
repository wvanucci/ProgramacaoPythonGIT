n = int(input('Digite um número inteiro para verificar se o número é divisivel por 3 e por 5: '))
d5 = n%5
d3 = n%3
if d5 == 0 and d3 != d5:
    print(f'{n} é divisivel por 5 mas não por 3')
elif d3 == 0 and d3 != d5:
    print(f'{n} é divisivel por 3 mas não por 5')

