num = int(input('Digite um número inteiro de até quatro dígitos: '))
u = num // 1 % 10   # // divisão inteiro  %resto da divisão
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('A unidade vale {}'.format(u))
print('A dezena vale {}'.format(d))
print('A centena vale {}'.format(c))
print('A milhar vale {}'.format(m))

print('A soma dos algarismos vale {}'.format(u + d + c + m))