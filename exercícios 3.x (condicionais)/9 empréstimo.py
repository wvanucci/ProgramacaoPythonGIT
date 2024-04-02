salário = float(input('Qual é o salário: '))
valorDePrestaçãoDoEmprestimo = float(input('Qual o valor da prestação: '))

if valorDePrestaçãoDoEmprestimo > 0.2*salário:
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedio')

