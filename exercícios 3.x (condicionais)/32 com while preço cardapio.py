"""
cachorroQuente = 100 preco 1.2
bauruSimples = 101  preco 1.3
bauruComOvo = 102  preco 1.5
hamburguer =103  preco 1.7
cheesburguer = 104 ...
suco = 105  ...
refrigerante = 106   ...
"""

conta = 0
while conta > -1:
    a = int(input('Qual o seu pedido? '))
    if a == 100:
        conta += 1.20
        b = input('Quer algo mais [S/N]? ')
        if b == 'N' or b == 'n':
            break
    elif a == 101:
        conta += 1.25
        b = input('Quer algo mais [S/N]? ')
        if b == 'N' or b == 'n':
            break
    elif a == 102:
        conta += 1.3
        b = input('Quer algo mais [S/N]? ')
        if b == 'N' or b == 'n':
            break
    elif a == 103:
        conta += 1.5
        b = input('Quer algo mais [S/N]? ')
        if b == 'N' or b == 'n':
            break
    elif a == 104:
        conta +=1.7
        b = input('Quer algo mais [S/N]? ')
        if b == 'N' or b == 'n':
            break
    elif a == 105:
        conta += 2.20
        b = input('Quer algo mais [S/N]? ')
        if b == 'N' or b == 'n':
            break
    elif a == 106:
        conta += 1
        b = input('Quer algo mais [S/N]? ')
        if b == 'N' or b == 'n':
            break
    elif (a < 100) or (a > 106):
        print('Não temos essa opção')
        b = input('Quer algo mais [S/N]? ')
        if b == 'N' or b == 'n':
            break

print(f'A  sua conta deu R${conta}')


