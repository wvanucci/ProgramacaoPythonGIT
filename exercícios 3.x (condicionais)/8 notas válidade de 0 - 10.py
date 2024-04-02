n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

if 0 <= n1 <= 10 and 0 <= n2 <= 10:
    media = (n1+n2)/2
    print(f'A nota 1 é {n1} e a nota 2 é {n2}. A média é {media}')
elif n1>= 10 or  n1 <= 0:
    print(f'a nota {n1} é inválida')
elif n2>= 10 or  n2 <= 0:
    print(f'A nota {n2} é inválida')

