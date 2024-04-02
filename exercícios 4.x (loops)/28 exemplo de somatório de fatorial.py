#somatório do tipo E = 1+1/n!
def serie_de_um_fatorial():
    print('Série do tipo E(n) = 1 + 1/2 + ... 1/n!')
    n = int(input('Digite n: '))
    e_n = 0
    mult = 1
    for i in range(1,n+1):
        mult *= i
        e_n +=1/mult

    print(f'A série E(n) até n = {n} é {e_n}.\n FATORIAL DE {n}: {mult}')

serie_de_um_fatorial()