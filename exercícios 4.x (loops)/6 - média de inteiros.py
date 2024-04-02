cont = 1
soma = 0
while cont < 11:
    valor = int(input(f'Qual o seu {cont}º valor: '))
    cont +=1
    soma += valor
print(cont)  #teste para mostrar o contador
media = soma/(cont-1)
print(f'A soma dos teus valores são {soma} e sua {media}')