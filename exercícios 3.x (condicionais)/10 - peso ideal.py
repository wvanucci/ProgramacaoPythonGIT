# peso ideal para homem e mulher
altura = float(input('Qual sua altura em metros: '))
sexo = input('Qual seu sexo: ')
sexoNormalizado = sexo.lower()
if sexoNormalizado == 'masculino' or sexoNormalizado == 'homem' or sexoNormalizado == 'm':
    pM = (72.7*altura) - 58
    print(f'Seu peso ideal é {pM}')
elif sexoNormalizado == 'mulher' or sexoNormalizado == 'feminino' or sexoNormalizado == 'f':
    pF = (62.1*altura) - 44.7
    print(f'Seu peso ideal é {pF}')


