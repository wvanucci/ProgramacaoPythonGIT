idade = int(input('Qual sua idade: '))
tempTrab = int(input('Tempo de trabalho (em anos): '))
if idade >= 65 or tempTrab >= 30 or (25 <= tempTrab < 30 and 60 <= idade < 65):
    print('Já pode se aposentar')
else:
    print('Não pode se aposentar')

