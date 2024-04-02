# área do trapézio
baseMaior = float(input('Qual é a base maior: '))
baseMenor = float(input('Qual é a base menor: '))
altura = float(input('Qual é altura: '))
area = (baseMaior+baseMenor)*altura/2
if baseMenor > 0 and baseMaior > 0:
    print(f'A área do trapézio é {area}')
else:
    print(f'Tem certeza que é um trapézio?')

