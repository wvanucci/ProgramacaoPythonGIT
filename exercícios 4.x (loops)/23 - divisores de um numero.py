numer = int(input('Digite um número: '))
for i in range(1,numer+1):
    if numer%i == 0:
        print(f'{numer} é divisível por {i}')
