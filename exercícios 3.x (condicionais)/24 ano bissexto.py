"""bissexto divisivel por 400 ou 4 (resto da divisão igual a zero)
e nao é divisivel por 100 (resto da divisão diferente de zero)
"""

ano = int(input('Qual o ano: '))

if (ano%400 == 0 or ano%4 == 0) and ano%100 != 0:
    print('Bissexto')
else:
    print('não é bissexto')

