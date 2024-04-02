soma = 0
cont =0
while cont >= 0:
    cont += 1
    idade = input('Qual a idade? Digite X para sair: ').lower().strip()
    if idade == 'x' or int(idade) <= 0:
        break
    elif int(idade) >0:
        soma += int(idade)
        medi = soma/cont

print(f'Média das idades {medi:.3f}')



