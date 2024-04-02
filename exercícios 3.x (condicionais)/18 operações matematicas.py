a = '_'*10
operadores = input(f'{a}OPERAÇÕES{a}\n'
               '[+] para adição\n'
               '[-] para subtração\n'
               '[/] para divisão\n'
               '[X] para multiplicação\n')
n1 = float(input('Você escolheu a operação. Qual seu primeiro número? '))
n2 = float(input('Qual seu segundo número: '))
if operadores == '+':
    print(f'{n1} + {n2} = {n1+n2}')
elif operadores == '-':
    print(f'{n1} - {n2} = {n1-n2}')
elif operadores == '/' and n2 != 0:
    print(f'{n1} dividio por {n2} é {n1/n2}')
elif operadores == 'x' or operadores == 'X':
    print(f'{n1} X {n2} = {n1*n2}')