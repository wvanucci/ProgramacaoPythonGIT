cont = 1
soma = 0
while cont < 11:
    valor = int(input(f'Qual o seu {cont}º valor: '))
    if valor > 0:
        cont +=1
        soma += valor
    else:
        print('Repita o procedimento')
print(cont)  #teste para mostrar o contador
media = soma/(cont-1)
print(f'A soma dos teus valores são {soma} e sua {media}')