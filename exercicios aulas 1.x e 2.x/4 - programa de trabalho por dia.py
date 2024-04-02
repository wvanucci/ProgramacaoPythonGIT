"""encanador trabalha 30,00 reais por dia. Qual a qunatiade líquida se são descontados 8% do imposto de renda
"""
nome = input('Qual o seu nome? ')
dias = int(input('Quantos dias de trabalho: '))
bruto = 30.00*dias
líquido = bruto-bruto*0.08
print(f'O senhor(a) {nome} trabalhou {dias} dias e deve receber um valor  líquido de R${líquido}. '
      f'O valor bruto é R${bruto}')
