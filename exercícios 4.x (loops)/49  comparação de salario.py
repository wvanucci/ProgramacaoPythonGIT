"""
Sálario de Carlos = joão/3. Sálario de carlos é integral na poupança que rende 2% ao mês. João aplica na renda fixa
rende 5% ao mês. Calcular e mostrar a quantidade de meses para o valor de João ser igual ou ultrapassar de carlos
"""

carlos = float(input('Sálario de Carlos: '))
joão = (carlos/3)
print('LEMBRE QUE A TAXA DE JUROS DE JOÃO É A MAIRO Q DE CARLOS')
jurosJoao = float(input('Digite o juros da aplicação de João: '))
jurosCarlos = float(input('Digite o juros da aplicação de Carlos: '))
RenMesC, RenMmesJ, mes =carlos,joão,0
while True:
    mes += 1
    RenMesC *= (1+jurosCarlos)
    RenMmesJ *= (1+jurosCarlos)
    if RenMmesJ > RenMesC:
        break

print(f'O invenstimento inicial de Carlos é {carlos} e de João é {joão}.\nDepois de {mes} meses João vai ter rendimento'
      f'de {RenMmesJ:.3f} e Carlos de {RenMesC:.3f}')
