import random
c = 0
numero = random.randint(1,1000)
while c>=0:
    c+=1
    qual = int(input('Qual o número? '))
    if qual > numero:
        print('O número que você digitou é maior que o desejado\n')
    elif qual < numero:
        print('O número que você digitou é menor que o desejado\n')
    elif qual == numero:
        print(f'Parabéns! Você acertou na {c}ª tentativa')
        break


