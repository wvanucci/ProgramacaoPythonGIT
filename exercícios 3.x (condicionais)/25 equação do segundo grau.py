print('equação do segundo grau na forma ax²+bx+c=0 ')
a = float(input('Qual o valor do coeficiente a: '))
b = float(input('Qual o valor do coeficiente b: '))
c = float(input('Qual o valor do coeficiente c: '))

if a == 0:
    x = -c/b
    print(f' Não é uma equação de segundo grau!\n A única raiz é {x}')
elif a!=0:
    delta = b**2-4*c*a
    if delta > 0:
        x1 = (-b + (delta)**(1/2))/(2*a)
        x2 = (-b - (delta)**(1/2))/(2*a)
        print(f'A raizes são {x1} e {x2}')
    elif delta == 0:
        x3 = -b/(2*a)
        print(f'Existe uma única raiz {x3}')
    elif delta < 0:
        print('Raizes são complexas. Não existe raiz real!')
else:
    print('Inválido')